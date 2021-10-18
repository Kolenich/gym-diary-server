"""Models for workouts app."""
from django.db import models


class Workout(models.Model):
    """Base workouts model."""

    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        db_table = 'workouts'

    @property
    def duration(self):
        end_minutes = self.end.hour * 60 + self.end.minute
        start_minutes = self.start.hour * 60 + self.start.minute
        return (end_minutes - start_minutes) / 60


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
