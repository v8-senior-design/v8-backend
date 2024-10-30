from django.contrib import admin
from .models import Emission, EmissionCategory, EmissionFactor


admin.site.register(EmissionCategory)
admin.site.register(Emission)
admin.site.register(EmissionFactor)
