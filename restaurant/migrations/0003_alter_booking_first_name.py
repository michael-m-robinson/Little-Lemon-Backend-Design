# Generated by Django 4.2.7 on 2023-12-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(max_length=200),
        ),
    ]
