# Generated by Django 5.0.1 on 2024-01-06 02:14

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('track', '0002_objective'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='objective',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_objectives', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='goal',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_goals', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('due_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=100)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('objective', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='objective_tasks', to='track.objective')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tasks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
