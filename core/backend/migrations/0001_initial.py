# Generated by Django 4.2.7 on 2023-11-19 21:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('palets', models.FloatField(max_length=4)),
                ('number_of_cases', models.IntegerField(max_length=4)),
                ('aile_numbers', models.CharField(max_length=60)),
                ('store_number', models.CharField(max_length=2)),
                ('lane_number', models.CharField(max_length=5)),
                ('time_started', models.DateTimeField(default=datetime.datetime(2023, 11, 19, 21, 9, 12, 734494))),
                ('time_finished', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='StoreTimes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('store_number', models.CharField(max_length=2)),
                ('hour_due', models.IntegerField(max_length=2)),
            ],
        ),
    ]
