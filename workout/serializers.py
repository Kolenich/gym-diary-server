"""Models serialization."""
from django.db import transaction
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

    def validate(self, attrs):
        start = attrs.get('start')
        end = attrs.get('end')

        if start >= end:
            raise serializers.ValidationError({
                'start': ['Начало тренировки должно быть раньше конца.'],
                'end': ['Конец тренировки должен быть позже начала.']
            })
        return super().validate(attrs)

    @transaction.atomic
    def create(self, validated_data):
        exercises = validated_data.pop('exercises')

        if not exercises:
            raise serializers.ValidationError({'exercises': ['Необходимо задать упражнения.']})

        instance = self.Meta.model.objects.create(**validated_data)

        exercises_serializer = ExerciseSerializer(
            data=list(map(lambda x: {**x, 'workout': instance}, exercises)),
            many=True
        )

        if exercises_serializer.is_valid(raise_exception=True):
            exercises_serializer.save()

        return instance
