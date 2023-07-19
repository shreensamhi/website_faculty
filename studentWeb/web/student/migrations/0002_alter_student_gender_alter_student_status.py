# Generated by Django 4.0.4 on 2022-05-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[(0, 'Male'), (1, 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[(0, 'Active'), (1, 'Inactive')], max_length=1),
        ),
    ]
