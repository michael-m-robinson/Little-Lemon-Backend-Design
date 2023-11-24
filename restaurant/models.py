from django.db import models


# Create your models here.

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(null=False)
    booking_date = models.DateTimeField();

    def __str__(self):
        return self.name


class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField(null=False)
    inventory = models.IntegerField(null=False, default=0)

    def __str__(self):
        return self.title