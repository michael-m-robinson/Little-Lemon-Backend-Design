from django.forms import ModelForm
from .models import Booking
from django.contrib.auth.models import User


# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"


class RegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
