# Generated by Django 4.0.4 on 2022-05-26 09:11

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodels',
            name='modellogo',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='logos'),
        ),
    ]
