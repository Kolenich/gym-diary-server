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

    sets = SetSerializer(many=True, required=False)

    class Meta:
        model = Exercise
        exclude = ['workout']

    @transaction.atomic
    def create(self, validated_data):
        """
        Override of create method, so it can handle nested creations.

        :param validated_data: validated data
        :return: created instance
        """
        sets = validated_data.pop('sets', [])

        instance = self.Meta.model.objects.create(**validated_data)

        if sets:
            sets_data = [{**x, 'exercise_id': instance.pk} for x in sets]
            sets_serializer = SetSerializer(data=sets_data, many=True)

            if sets_serializer.is_valid(raise_exception=True):
                sets_serializer.save()

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        Override of update method so it can handle nested creations.

        :param instance: instance to be updated
        :param validated_data: validated data
        :return: updated instance
        """
        sets = validated_data.pop('sets', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save(update_fields=validated_data.keys())

        if sets:
            sets_data = [{**x, 'exercise_id': instance.pk} for x in sets]
            sets_serializer = SetSerializer(data=sets_data, many=True)

            if sets_serializer.is_valid(raise_exception=True):
                sets_serializer.save()

        return instance


class WorkoutSerializer(serializers.ModelSerializer):
    """Base workouts model serializer."""

    exercises = ExerciseSerializer(many=True, required=False)

    class Meta:
        model = Workout
        fields = '__all__'

    def validate(self, attrs):
        """
        Override of validate method to add additional validations.

        :param attrs: data to be validated
        :return: validated data
        """
        start = attrs.get('start')
        end = attrs.get('end')

        if start >= end:
            raise serializers.ValidationError({
                'start': ['Начало тренировки должно быть раньше конца.'],
                'end': ['Конец тренировки должен быть позже начала.']
            })
        # Validating duration being not longer than 2 hours
        end_minutes = end.hour * 60 + end.minute
        start_minutes = start.hour * 60 + start.minute
        hours = (end_minutes - start_minutes) / 60

        if hours > 2:
            raise serializers.ValidationError({
                'start': ['Тренировка не должна превышать 2 часа.'],
                'end': ['Тренировка не должна превышать 2 часа.']
            })

        return super().validate(attrs)

    @transaction.atomic
    def create(self, validated_data):
        """
        Override of create method, so it can handle nested creations.

        :param validated_data: validated data
        :return: created instance
        """
        exercises = validated_data.pop('exercises', [])

        instance = self.Meta.model.objects.create(**validated_data)

        if exercises:
            exercises_data = [{**x, 'workout_id': instance.pk} for x in exercises]
            exercises_serializer = ExerciseSerializer(data=exercises_data, many=True)

            if exercises_serializer.is_valid(raise_exception=True):
                exercises_serializer.save()

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        """
        Override of update method so it can handle nested creations.

        :param instance: instance to be updated
        :param validated_data: validated data
        :return: updated instance
        """
        exercises = validated_data.pop('exercises', [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save(update_fields=validated_data.keys())

        if exercises:
            exercises_data = [{**x, 'workout_id': instance.pk} for x in exercises]
            exercises_serializer = ExerciseSerializer(data=exercises_data, many=True)

            if exercises_serializer.is_valid(raise_exception=True):
                exercises_serializer.save()

        return instance


class WorkoutListSerializer(serializers.ModelSerializer):
    """Simple list serializer for workouts."""

    class Meta:
        model = Workout
        fields = '__all__'
