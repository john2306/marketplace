# Generated by Django 4.0.4 on 2022-04-30 18:17

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_categoria_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True),
        ),
    ]
