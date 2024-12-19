"""Workout app views."""
from rest_framework import viewsets

from .models import Exercise, Workout, Set
from .serializers import ExerciseSerializer, SetSerializer, WorkoutSerializer


class WorkoutViewset(viewsets.ModelViewSet):
    """Workouts model viewset."""

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
    filterset_fields = {
        'start': ('gte', 'lte'),
        'end': ('gte', 'lte')
    }


class ExerciseViewset(viewsets.ModelViewSet):
    """Exercises model viewset."""

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filterset_fields = ('workout_id',)


class SetViewset(viewsets.ModelViewSet):
    """Sets model viewset."""

    queryset = Set.objects.all()
    serializer_class = SetSerializer
    filterset_fields = ('exercise_id',)
