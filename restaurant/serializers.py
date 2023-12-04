from rest_framework.serializers import ModelSerializer
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from .models import Menu, Booking

User = get_user_model()


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        fields = ["id", "username", "email", "first_name", "last_name", "groups"]


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ["id", "name", "price", "menu_item_description"]


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
