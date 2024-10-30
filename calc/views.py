from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Emission, EmissionCategory, EmissionFactor
from .serializers import EmissionSerializer, EmissionCategorySerializer, EmissionFactorSerializer


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
