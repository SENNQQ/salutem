# Generated by Django 4.0.2 on 2022-03-23 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0014_analyzes_show'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='Sex',
            field=models.CharField(blank=True, choices=[('Женщина', 'Женщина'), ('Мужчина', 'Мужчина')], max_length=20),
        ),
    ]