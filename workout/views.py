"""Workout app views."""
from rest_framework import viewsets

from .models import Workout
from .serializers import WorkoutSerializer


class WorkoutViewset(viewsets.ModelViewSet):
    """Base workout model viewset."""

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
