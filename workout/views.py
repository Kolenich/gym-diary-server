"""Workout app views."""
from django.db import transaction
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Workout
from .serializers import ExerciseSerializer, SetSerializer, WorkoutSerializer


class WorkoutViewset(viewsets.ModelViewSet):
    """Base workout model viewset."""

    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        exercises_data = request.data.pop('exercises')

        new_exercises = list(filter(lambda x: isinstance(x.get('id'), str), exercises_data))
        existing_exercises = list(filter(lambda x: isinstance(x.get('id'), int), exercises_data))

        workout_instance = self.get_object()
        workout_data = request.data

        workout_serializer = self.get_serializer(
            instance=workout_instance,
            data={**workout_data, 'exercises': new_exercises}
        )

        if workout_serializer.is_valid(raise_exception=True):
            workout_serializer.save()

        # Creating/updating exercises
        for exercise in existing_exercises:
            sets = exercise.pop('sets')

            new_sets = list(filter(lambda x: isinstance(x.get('id'), str), sets))
            existing_sets = list(filter(lambda x: isinstance(x.get('id'), int), sets))

            exercise_instance = self.get_object().exercises.get(pk=exercise.get('id'))

            exercise_serializer = ExerciseSerializer(
                instance=exercise_instance,
                data={**exercise, 'sets': new_sets}
            )

            if exercise_serializer.is_valid(raise_exception=True):
                exercise_serializer.save()

            # Creating/updating sets
            for set_ in existing_sets:
                set_instance = exercise_instance.sets.get(pk=set_.get('id'))

                set_serializer = SetSerializer(instance=set_instance, data=set_)
                if set_serializer.is_valid(raise_exception=True):
                    set_serializer.save()

        return Response(workout_serializer.data)
