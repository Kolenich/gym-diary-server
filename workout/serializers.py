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

    def create(self, validated_data):
        exercises = validated_data.pop('exercises')

        if validated_data.get('start') and not validated_data.get('end'):
            raise serializers.ValidationError({'end': ['Необходимо указать конец тренировки.']})

        if validated_data.get('end') and not validated_data.get('start'):
            raise serializers.ValidationError({'start': ['Необходимо указать начало тренировки.']})

        if not exercises:
            raise serializers.ValidationError({'exercises': ['Необходимо задать упражнения.']})

        instance = self.Meta.model.objects.create(**validated_data)

        return instance
