# Generated by Django 5.0.3 on 2024-05-05 05:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disc', '0004_rename_ordered_on_order_booked_on'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cs_name', models.CharField(max_length=255)),
                ('cs_phno', models.CharField(max_length=255)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disc.movies')),
            ],
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
