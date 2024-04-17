"""URL-patterns for workouts app."""
from rest_framework import routers

from .views import WorkoutViewset

ROUTER = routers.DefaultRouter(trailing_slash=False)
ROUTER.register('workouts', WorkoutViewset)


urlpatterns = ROUTER.urls
