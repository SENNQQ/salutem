# Generated by Django 4.0.2 on 2022-02-23 12:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0003_analyzes_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyzes',
            name='patient',
        ),
        migrations.AddField(
            model_name='analyzes',
            name='patient',
            field=models.ManyToManyField(to='patients.Patients'),
        ),
        migrations.RemoveField(
            model_name='analyzes',
            name='specialist',
        ),
        migrations.AddField(
            model_name='analyzes',
            name='specialist',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
