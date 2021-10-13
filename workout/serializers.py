"""Models serialization."""
from rest_framework import serializers

from .models import Exercise, Set, Workout


class SetSerializer(serializers.ModelSerializer):
    """Base set serializer."""

    class Meta:
        model = Set
        exclude = ['exercise']


class ExerciseSerializer(serializers.ModelSerializer):
    """Base exercise model serializer."""

    sets = SetSerializer(many=True)

    class Meta:
        model = Exercise
        exclude = ['workout']


class WorkoutSerializer(serializers.ModelSerializer):
    """Base workout model serializer."""

    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Workout
        fields = '__all__'
