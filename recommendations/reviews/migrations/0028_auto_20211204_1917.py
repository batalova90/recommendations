# Generated by Django 2.2.19 on 2021-12-04 19:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0027_auto_20211204_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='text',
            field=ckeditor.fields.RichTextField(),
        ),
    ]