# Generated by Django 4.0.2 on 2022-02-23 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_patients_data_joined'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzes',
            name='result',
            field=models.TextField(null=True),
        ),
    ]
