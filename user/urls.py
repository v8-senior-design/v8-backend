from django.urls import path
from .views import test_view

urlpatterns = [
    path('register/', view=test_view, name='register'),
    path('login/', view=test_view, name='login'),
    path('forgot/', view=test_view, name='forgot'),
]
