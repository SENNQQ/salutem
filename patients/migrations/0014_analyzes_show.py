# Generated by Django 4.0.2 on 2022-03-13 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0013_alter_analyzes_date_of_change'),
    ]

    operations = [
        migrations.AddField(
            model_name='analyzes',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
