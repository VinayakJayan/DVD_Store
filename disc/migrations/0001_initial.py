# Generated by Django 5.0.3 on 2024-04-29 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_name', models.CharField(max_length=255)),
                ('c_phone', models.CharField(max_length=255)),
                ('c_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pic')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cs_name', models.CharField(max_length=255)),
                ('cs_phno', models.CharField(max_length=255)),
                ('booking_date', models.DateField()),
                ('booked_on', models.DateField(auto_now=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disc.movies')),
            ],
        ),
    ]