# Generated by Django 2.2.19 on 2021-11-19 16:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0007_reviews_raiting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='raiting',
        ),
        migrations.AlterField(
            model_name='raitingreview',
            name='raiting',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
