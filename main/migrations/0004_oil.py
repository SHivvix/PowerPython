# Generated by Django 5.1.1 on 2024-10-07 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_metervalue_value_metervalue_value_fact_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Oil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('value', models.FloatField()),
            ],
        ),
    ]