from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Emission, EmissionCategory, EmissionFactor
from .serializers import EmissionSerializer, EmissionCategorySerializer, EmissionFactorSerializer
from django.db.models import Sum, Count, F, Min
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model


User = get_user_model()

class EmissionCategoryViewSet(viewsets.ModelViewSet):
    queryset = EmissionCategory.objects.all()
    serializer_class = EmissionCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EmissionFactorViewSet(viewsets.ModelViewSet):
    queryset = EmissionFactor.objects.all()
    serializer_class = EmissionFactorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class EmissionViewSet(viewsets.ModelViewSet):
    serializer_class = EmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date']

    def get_queryset(self):
        return Emission.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LeaderboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        try:
            user_averages = (
                Emission.objects
                .values('user')
                .annotate(
                    total_emissions=Sum('total_emissions_kg'),
                    first_recorded_date=Min('date'),
                    days_on_platform=Count('date', distinct=True),
                )
                .annotate(
                    average_co2_per_day=F('total_emissions') / F('days_on_platform')
                )
                .order_by('average_co2_per_day')[:50]
            )

            leaderboard = []
            for entry in user_averages:
                user = User.objects.get(id=entry['user'])
                first_name = user.first_name
                last_name_initial = f"{user.last_name[0]}." if user.last_name else ""

                leaderboard.append({
                    'user': f"{first_name} {last_name_initial}".strip(),
                    'average_co2_per_day': round(entry['average_co2_per_day'], 2),
                    'days_on_platform': entry['days_on_platform']
                })

            return Response(leaderboard)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
