"""Models for workout app."""
from django.db import models


class Workout(models.Model):
    """Base workout model."""

    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    class Meta:
        db_table = 'workouts'


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
