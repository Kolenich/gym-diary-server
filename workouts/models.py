"""Models for workouts app."""
import json

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from workouts.consumers import WorkoutConsumer


class Workout(models.Model):
    """Base workouts model."""

    date = models.DateField()
    start_time = models.TimeField()
    duration_hours = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(2)])
    focus_area = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = 'workouts'

    def to_websocket(self, action):
        channel_layer = get_channel_layer()

        async_to_sync(channel_layer.group_send)(WorkoutConsumer.group, {
            'type': 'workout.inform',
            'message': json.dumps({'action': action, 'arg': self.id}),
        })


class Exercise(models.Model):
    """Base exercise model."""

    name = models.CharField(max_length=128)
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE, related_name='exercises')

    class Meta:
        db_table = 'exercises'


class Set(models.Model):
    """Base model for set. Each set can have various repeats and weight."""

    weight = models.PositiveSmallIntegerField()
    repeats = models.PositiveSmallIntegerField()
    exercise = models.ForeignKey('Exercise', on_delete=models.CASCADE, related_name='sets')

    class Meta:
        db_table = 'sets'
