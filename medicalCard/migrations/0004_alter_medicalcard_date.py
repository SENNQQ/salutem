# Generated by Django 4.0.2 on 2022-04-02 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalCard', '0003_medicalcard_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalcard',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
