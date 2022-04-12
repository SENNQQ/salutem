# Generated by Django 4.0.2 on 2022-04-12 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0016_rename_test_date_analyzes_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sicklist', '0006_alter_sicklist_address_of_md_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sicklist',
            name='patient',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='patients.patients'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sicklist',
            name='public_organizations',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='sicklist',
            name='specialist',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
