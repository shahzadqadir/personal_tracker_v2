# Generated by Django 5.0.1 on 2024-01-06 02:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0005_alter_goal_status_alter_task_end_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]