# Generated by Django 4.2.15 on 2024-12-20 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_rename_duration_workout_duration_hours'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='start',
            new_name='start_time',
        ),
    ]