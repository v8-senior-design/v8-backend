from django.urls import path
from user.views import test_view

urlpatterns = [
    path('cf_get/', view=test_view, name='cf_get'),
    path('cf_post/', view=test_view, name='cf_post'),
    path('leaderboard_get/', view=test_view, name='leaderboard_get'),
]
