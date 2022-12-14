# Generated by Django 4.0.2 on 2022-02-23 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('patients', '0004_remove_analyzes_patient_analyzes_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analyzes',
            name='patient',
        ),
        migrations.AddField(
            model_name='analyzes',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.patients'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='analyzes',
            name='specialist',
        ),
        migrations.AddField(
            model_name='analyzes',
            name='specialist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='analyzes',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patients.analyzestype'),
        ),
    ]
