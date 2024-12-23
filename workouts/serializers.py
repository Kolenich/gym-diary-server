"""Models serialization."""
from rest_framework import serializers

from .models import Exercise, Set, Workout


class SetSerializer(serializers.ModelSerializer):
    """Base set serializer."""

    exercise_id = serializers.IntegerField()

    class Meta:
        model = Set
        exclude = ('exercise',)


class ExerciseSerializer(serializers.ModelSerializer):
    """Base exercise model serializer."""

    workout_id = serializers.IntegerField()

    class Meta:
        model = Exercise
        exclude = ('workout',)


class WorkoutSerializer(serializers.ModelSerializer):
    """Simple serializer for workouts."""

    start_time = serializers.TimeField(format='%H:%M')

    class Meta:
        model = Workout
        fields = '__all__'
