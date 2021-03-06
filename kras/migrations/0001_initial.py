# Generated by Django 3.0.4 on 2020-04-02 09:41

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
            name='Kra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('startDate', models.DateTimeField()),
                ('endDate', models.DateTimeField()),
                ('percentageTotalPlanned', models.IntegerField(null=True)),
                ('percentageTotalAchieved', models.IntegerField(null=True)),
                ('quarter', models.CharField(blank=True, max_length=20)),
                ('year', models.IntegerField()),
                ('managerObservation', models.CharField(max_length=1000)),
                ('selfObservation', models.CharField(max_length=1000)),
                ('thresholdStatus', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
