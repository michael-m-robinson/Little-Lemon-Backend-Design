# Generated by Django 4.2.7 on 2023-11-25 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_booking_booking_date_remove_booking_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.FloatField(),
        ),
    ]
