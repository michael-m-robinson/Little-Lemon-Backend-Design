from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuTest(TestCase):
    def setUp(self):
        self.item1 = Menu(title="IceCream", price=5.80, inventory=100)
        self.item2 = Menu(title="Pizza", price=10.80, inventory=100)
        self.item3 = Menu(title="Burger", price=5.50, inventory=100)

    def test_get_all(self):
        # Create serialized items
        serialized_item_one = MenuSerializer(self.item1, many=False)
        serialized_item_two = MenuSerializer(self.item2, many=False)
        serialized_item_three = MenuSerializer(self.item3, many=False)

        # check for accuracy
        self.assertEqual(str(serialized_item_one.data), "{'title': 'IceCream', 'price': 5.8, 'inventory': 100}")
        self.assertEqual(str(serialized_item_two.data), "{'title': 'Pizza', 'price': 10.8, 'inventory': 100}")
        self.assertEqual(str(serialized_item_three.data), "{'title': 'Burger', 'price': 5.5, 'inventory': 100}")
