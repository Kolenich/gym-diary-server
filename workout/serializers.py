"""Models serialization."""
from django.db import transaction
from rest_framework import serializers

from .models import Exercise, Set, Workout


class SetSerializer(serializers.ModelSerializer):
    """Base set serializer."""
    exercise_id = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        model = Set
        exclude = ['exercise']


class ExerciseSerializer(serializers.ModelSerializer):
    """Base exercise model serializer."""
    workout_id = serializers.IntegerField(required=False, write_only=True)
    sets = SetSerializer(many=True)

    class Meta:
        model = Exercise
        exclude = ['workout']

    @transaction.atomic
    def create(self, validated_data):
        sets = validated_data.pop('sets')

        if not sets:
            raise serializers.ValidationError({'sets': ['Необходимо указать подходы.']})

        instance = self.Meta.model.objects.create(**validated_data)

        sets_data = list(map(lambda x: {**x, 'exercise_id': instance.pk}, sets))

        sets_serializer = SetSerializer(data=sets_data, many=True)

        if sets_serializer.is_valid(raise_exception=True):
            sets_serializer.save()

        return instance


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

        exercises_data = list(map(lambda x: {**x, 'workout_id': instance.pk}, exercises))

        exercises_serializer = ExerciseSerializer(data=exercises_data, many=True)

        if exercises_serializer.is_valid(raise_exception=True):
            exercises_serializer.save()

        return instance
