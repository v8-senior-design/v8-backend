from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmissionViewSet, EmissionCategoryViewSet, EmissionFactorViewSet


router = DefaultRouter()
router.register(r'emission-categories', EmissionCategoryViewSet, basename='emission-category')
router.register(r'emission-factors', EmissionFactorViewSet, basename='emission-factor')
router.register(r'emissions', EmissionViewSet, basename='emission')

urlpatterns = [
    path('', include(router.urls)),
]
