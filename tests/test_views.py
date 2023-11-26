from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuTest(TestCase):
    def setUp(self):
        self.item1 = Menu(name="IceCream", price=5.80, menu_item_description="Little Lemon IceCream")
        self.item2 = Menu(name="Pizza", price=10.80, menu_item_description="Little Lemon Pizza")
        self.item3 = Menu(name="Burger", price=5.50, menu_item_description="Little Lemon Burger")

    def test_get_all(self):
        # Create serialized items
        serialized_item_one = MenuSerializer(self.item1, many=False)
        serialized_item_two = MenuSerializer(self.item2, many=False)
        serialized_item_three = MenuSerializer(self.item3, many=False)

        # check for accuracy
        self.assertEqual(str(serialized_item_one.data), "{'name': 'IceCream', 'price': 5.8, 'menu_item_description': 'Little Lemon IceCream'}")
        self.assertEqual(str(serialized_item_two.data), "{'name': 'Pizza', 'price': 10.8, 'menu_item_description': 'Little Lemon Pizza'}")
        self.assertEqual(str(serialized_item_three.data), "{'name': 'Burger', 'price': 5.5, 'menu_item_description': 'Little Lemon Burger'}")
