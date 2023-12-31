# Generated by Django 4.0.4 on 2022-05-22 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.CharField(max_length=100)),
                ('studentid', models.IntegerField(max_length=8)),
                ('birthday', models.DateField()),
                ('gpa', models.DecimalField(decimal_places=2, max_digits=3)),
                ('level', models.CharField(max_length=10)),
                ('gender', models.BooleanField()),
                ('email', models.EmailField(max_length=50)),
                ('phonenumber', models.IntegerField(max_length=11)),
                ('department', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
