# Generated by Django 3.1.5 on 2021-02-08 13:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resourcecenter', '0008_auto_20210208_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]