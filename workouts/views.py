"""Workout app views."""
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets

from .models import Exercise, Set, Workout
from .serializers import ExerciseSerializer, SetSerializer, WorkoutSerializer

WORKOUTS_TAG = ('Workouts',)
EXERCISES_TAG = ('Exercises',)
SETS_TAG = ('Sets',)


@extend_schema_view(
    list=extend_schema(description='List of Workouts', tags=WORKOUTS_TAG),
    retrieve=extend_schema(description='Get single Workout', tags=WORKOUTS_TAG),
    update=extend_schema(description='Full Workout update', tags=WORKOUTS_TAG),
    partial_update=extend_schema(description='Partial Workout update', tags=WORKOUTS_TAG),
    create=extend_schema(description='Create single Workout', tags=WORKOUTS_TAG),
    destroy=extend_schema(description='Delete Workout', tags=WORKOUTS_TAG),
)
class WorkoutViewset(viewsets.ModelViewSet):
    """Workouts model viewset."""

    queryset = Workout.objects.order_by('start_time')
    serializer_class = WorkoutSerializer
    filterset_fields = {
        'date': ('exact',),
        'focus_area': ('icontains',)
    }
    ordering_fields = ('date', 'start_time', 'duration_hours')


@extend_schema_view(
    list=extend_schema(description='List of Exercises', tags=EXERCISES_TAG),
    retrieve=extend_schema(description='Get single Exercise', tags=EXERCISES_TAG),
    update=extend_schema(description='Full Exercise update', tags=EXERCISES_TAG),
    partial_update=extend_schema(description='Partial Exercise update', tags=EXERCISES_TAG),
    create=extend_schema(description='Create single Exercise', tags=EXERCISES_TAG),
    destroy=extend_schema(description='Delete Exercise', tags=EXERCISES_TAG),
)
class ExerciseViewset(viewsets.ModelViewSet):
    """Exercises model viewset."""

    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    filterset_fields = ('workout_id',)


@extend_schema_view(
    list=extend_schema(description='List of Sets', tags=SETS_TAG),
    retrieve=extend_schema(description='Get single Set', tags=SETS_TAG),
    update=extend_schema(description='Full Set update', tags=SETS_TAG),
    partial_update=extend_schema(description='Partial Set update', tags=SETS_TAG),
    create=extend_schema(description='Create single Set', tags=SETS_TAG),
    destroy=extend_schema(description='Delete Set', tags=SETS_TAG),
)
class SetViewset(viewsets.ModelViewSet):
    """Sets model viewset."""

    queryset = Set.objects.all()
    serializer_class = SetSerializer
    filterset_fields = ('exercise_id',)
