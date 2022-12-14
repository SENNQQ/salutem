# Generated by Django 4.0.2 on 2022-02-22 21:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalyzesType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=240)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sex', models.CharField(choices=[('Женщина', 'Женщина'), ('Мужчина', 'Мужчина')], max_length=20)),
                ('Name', models.CharField(max_length=100)),
                ('Surname', models.CharField(max_length=100)),
                ('Patronymic', models.CharField(max_length=100)),
                ('Date_of_birth', models.DateField(blank=True)),
                ('Place_of_residence', models.CharField(blank=True, max_length=100)),
                ('Blood_type', models.CharField(blank=True, choices=[('I+', 'I+'), ('II+', 'II+'), ('III+', 'III+'), ('IV+', 'IV+'), ('I-', 'I-'), ('II-', 'II-'), ('III-', 'III-'), ('IV-', 'IV-')], max_length=10)),
                ('Telephone', models.CharField(blank=True, max_length=100)),
                ('Email', models.CharField(blank=True, max_length=30)),
                ('photo', models.ImageField(blank=True, max_length=210, null=True, upload_to='photos/patient/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Analyzes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField()),
                ('date_of_change', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Новый', 'Новый'), ('В процессе', 'В процессе'), ('Выполнен', 'Выполнен')], default='Новый', max_length=20)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.patients')),
                ('specialist', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.analyzestype')),
            ],
        ),
    ]
