# Generated by Django 3.2.8 on 2021-10-15 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='workout',
            name='start',
            field=models.TimeField(),
        ),
    ]
