# Generated by Django 5.1.1 on 2024-10-01 11:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField()),
                ('date', models.DateField()),
                ('transmitting_side', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name='Meters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_meter', models.IntegerField()),
                ('name', models.CharField()),
                ('auto_collection', models.BooleanField(default=False)),
                ('id_consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.consumers')),
            ],
        ),
        migrations.CreateModel(
            name='MeterCoef',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meters')),
            ],
        ),
        migrations.CreateModel(
            name='Plase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField()),
                ('city', models.CharField()),
                ('id_agreement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.agreement')),
            ],
        ),
        migrations.CreateModel(
            name='MeterValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_first', models.FloatField()),
                ('value_last', models.FloatField()),
                ('value', models.FloatField()),
                ('date_add', models.DateField()),
                ('number_meter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.meters')),
                ('id_palse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plase')),
            ],
        ),
        migrations.AddField(
            model_name='meters',
            name='id_plase',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.plase'),
        ),
    ]
