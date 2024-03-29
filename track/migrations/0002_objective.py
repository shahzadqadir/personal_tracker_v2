# Generated by Django 5.0.1 on 2024-01-06 00:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('category', models.CharField(blank=True, max_length=100, null=True)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('completion_date', models.DateField(blank=True, null=True)),
                ('effort_hours', models.FloatField(default=2.0)),
                ('effort_hours_left', models.FloatField(default=2.0)),
                ('status', models.CharField(default='notdone', max_length=100)),
                ('progress', models.PositiveIntegerField(default=0)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='goal_objectives', to='track.goal')),
            ],
        ),
    ]
