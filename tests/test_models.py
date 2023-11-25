import datetime
import pytz

from django.test import TestCase
from restaurant.models import Menu, Booking
from django.conf import settings


class MenuTest(TestCase):
    def test_menu_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

    def test_booking_get_item(self):
        item = Booking.objects.create(name="Michael", no_of_guests=5,
                                      booking_date=datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE)))

        self.assertEqual(str(item), "Michael : 5")
