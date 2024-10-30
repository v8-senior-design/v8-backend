from rest_framework import serializers
from .models import Emission, EmissionCategory, EmissionFactor


class EmissionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionCategory
        fields = ['id', 'name']


class EmissionFactorSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=EmissionCategory.objects.all())

    class Meta:
        model = EmissionFactor
        fields = ['id', 'category', 'name', 'factor', 'unit']


class EmissionSerializer(serializers.ModelSerializer):
    emission_factor = serializers.PrimaryKeyRelatedField(queryset=EmissionFactor.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=EmissionCategory.objects.all())

    class Meta:
        model = Emission
        fields = ['id', 'user', 'date', 'category', 'emission_factor', 'quantity', 'total_emissions_kg']
        read_only_fields = ['user', 'total_emissions_kg']
