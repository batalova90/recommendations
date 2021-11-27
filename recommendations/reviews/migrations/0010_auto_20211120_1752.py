# Generated by Django 2.2.19 on 2021-11-20 17:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0009_auto_20211120_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creations',
            name='rating',
            field=models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
