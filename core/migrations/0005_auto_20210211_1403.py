# Generated by Django 3.1.5 on 2021-02-11 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210209_2110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='students',
        ),
        migrations.RemoveField(
            model_name='student',
            name='matric_number',
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.level'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
