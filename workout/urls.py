"""URL-patterns for workout app."""
from rest_framework import routers

from .views import WorkoutViewset

ROUTER = routers.DefaultRouter()
ROUTER.register('workouts', WorkoutViewset)

urlpatterns = ROUTER.urls
