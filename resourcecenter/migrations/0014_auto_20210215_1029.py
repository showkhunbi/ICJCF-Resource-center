# Generated by Django 3.1.5 on 2021-02-15 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resourcecenter', '0013_auto_20210215_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='file',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resourcecenter.file'),
        ),
    ]
