import datetime
import pytz

from django.test import TestCase
from restaurant.models import Menu, Booking
from django.conf import settings


class MenuTest(TestCase):
    def test_menu_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, menu_item_description="A little lemon classic, lemon ice cream with whip topping")
        self.assertEqual(str(item), "IceCream : 80")

    def test_booking_get_item(self):
        item = Booking.objects.create(first_name="Michael", reservation_slot=5,
                                      reservation_date=datetime.datetime.now(tz=pytz.timezone(settings.TIME_ZONE)))

        self.assertEqual(str(item), "Michael : 5")
