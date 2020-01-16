# Generated by Django 3.0.1 on 2020-01-16 06:47

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
            name='Reagent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=100)),
                ('CAT_number', models.IntegerField()),
                ('batch_number', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('marker', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('date_supplied', models.DateTimeField(blank=True, null=True)),
                ('manufacturer_date', models.DateTimeField(blank=True, null=True)),
                ('expiry_date', models.DateTimeField(blank=True, null=True)),
                ('storage_requirement', models.TextField()),
                ('location_in_lab', models.CharField(max_length=130)),
                ('ordered_by', models.CharField(max_length=130)),
                ('project_code', models.CharField(max_length=130)),
                ('data_entry_by', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
