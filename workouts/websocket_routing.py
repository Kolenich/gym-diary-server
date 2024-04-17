from django.urls import path

from .consumers import WorkoutConsumer

urlpatterns = [
    path('ws/workout', WorkoutConsumer.as_asgi()),
]
