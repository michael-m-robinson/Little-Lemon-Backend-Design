# Generated by Django 4.2.7 on 2023-11-25 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='booking_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='no_of_guests',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='title',
        ),
        migrations.AddField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default='Little Lemon Customer', max_length=200),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='No Description', max_length=1000),
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default='Please Fix me.', max_length=200),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(),
        ),
    ]
