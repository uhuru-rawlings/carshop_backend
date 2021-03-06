# Generated by Django 4.0.4 on 2022-05-26 07:03

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carmodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelname', models.CharField(max_length=300)),
                ('dateadded', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Carmodels',
            },
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('useremail', models.CharField(max_length=300)),
                ('username', models.EmailField(max_length=300)),
                ('passwords', models.CharField(max_length=300)),
                ('datedadded', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'Registration',
            },
        ),
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('engines_cc', models.IntegerField()),
                ('fueltype', models.CharField(max_length=200)),
                ('dimension_length', models.FloatField()),
                ('dimension_width', models.FloatField()),
                ('dimension_height', models.FloatField()),
                ('transmision', models.CharField(max_length=200)),
                ('capacity_weight', models.FloatField()),
                ('waranty_years', models.IntegerField()),
                ('price', models.IntegerField()),
                ('dateadded', models.DateTimeField(auto_now=True)),
                ('carmodel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.carmodels')),
            ],
            options={
                'db_table': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carimages', cloudinary.models.CloudinaryField(max_length=255, verbose_name='images')),
                ('dateadded', models.DateTimeField(auto_now=True)),
                ('car_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cars')),
            ],
            options={
                'db_table': 'CarImages',
            },
        ),
    ]
