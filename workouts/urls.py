"""URL-patterns for workouts app."""
from rest_framework import routers

from .views import WorkoutViewset, ExerciseViewset, SetViewset

ROUTER = routers.DefaultRouter(trailing_slash=False)
ROUTER.register('workouts', WorkoutViewset)
ROUTER.register('exercises', ExerciseViewset)
ROUTER.register('sets', SetViewset)

urlpatterns = ROUTER.urls
