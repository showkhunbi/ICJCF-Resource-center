# Generated by Django 3.1.5 on 2021-02-08 03:27

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resourcecenter', '0006_auto_20210208_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='file__name'),
        ),
    ]