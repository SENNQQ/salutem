# Generated by Django 4.0.2 on 2022-03-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_alter_analyzes_date_of_change'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analyzes',
            name='date_of_change',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
