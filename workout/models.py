"""Модели приложения workout."""
from django.db import models


class Workout(models.Model):
    """Модель тренировки."""
    date = models.DateField()
    start = models.TimeField(null=True, blank=True)
    end = models.TimeField(null=True, blank=True)


class Exercise(models.Model):
    """Модель упражнения."""

    name = models.CharField(max_length=128)
    weight = models.PositiveSmallIntegerField()
    repeats = models.PositiveSmallIntegerField()
    workout = models.ForeignKey('Workout', on_delete=models.CASCADE)
