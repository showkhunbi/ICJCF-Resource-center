# Generated by Django 3.1.5 on 2021-02-09 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resourcecenter', '0009_file_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonAcademicLevel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
