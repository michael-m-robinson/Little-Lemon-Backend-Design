from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from django.core import serializers
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .forms import BookingForm, RegistrationForm
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from datetime import datetime
from .models import Menu, Booking, UserAccount
import json


# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {"bookings": booking_json})


@login_required(login_url='/401/')
def book(request):
    if not request.user.is_authenticated:
        return render(request, 'restricted.html')
    elif request.user.is_authenticated:
        form = BookingForm()
        if request.method == 'POST':
            form = BookingForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'book.html', context)


def register(request):
    form = RegistrationForm()
    context = {'form': form}
    return render(request, 'register.html', context)


class LoginUser(CreateAPIView):
    def post(self, request, *args, **kwargs):
        if request.data:
            username = request.data['username']
            password = request.data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                response = Response({'message': 'Login successful 😊', 'token': token.key}, status=status.HTTP_200_OK)
                return response
            else:
                return Response({'message': 'Login failed 😒'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'could not find username and/or password.'}, status=status.HTTP_400_BAD_REQUEST)


def login_view(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(request, username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             token, created = Token.objects.get_or_create(user=user)
    #             response = JsonResponse({'message': 'Login successful 😊'})
    #             response.set_cookie('authToken', token.key, httponly=True, secure=True)
    #             return response
    #         else:
    #             return JsonResponse({'message': 'Login failed 😒'})

    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, 'menu_item.html', {"menu_item": menu_item})


def custom_401(request, exception=None):
    return render(request, '401.html', status=401)


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class UserViewSet(ModelViewSet):
    queryset = UserAccount.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


@permission_classes([IsAuthenticated])
class MenuItemView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_queryset(self):
        # Retrieve all menu items
        if self.request.user.is_superuser:
            return Menu.objects.all()
        else:
            return Response({'Message': 'You do not have permission to use this api.'},
                            status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request, *args, **kwargs):
        # Handle POST requests
        if self.request.user.is_superuser:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'You do not have permission to use this api.'},
                            status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get(self, request, *args, **kwargs):
        # Handle GET requests
        if self.request.user.is_superuser:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'You do not have permission to use this api.'},
                            status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, *args, **kwargs):
        # Handle PUT requests
        if self.request.user.is_superuser:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'You do not have permission to use this api.'},
                            status=status.HTTP_401_UNAUTHORIZED)

    def patch(self, request, *args, **kwargs):
        # Handle PATCH requests
        if self.request.user.is_superuser:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'Message': 'You do not have permission to use this api.'},
                            status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            instance = self.get_object()
            instance.delete()
            return Response({"message": "Object deleted successfully"})
        else:
            return Response({'Message': 'You do not have permission to use this api.'},
                            status=status.HTTP_401_UNAUTHORIZED)


@permission_classes([IsAuthenticated])
class SingleBookingItem(RetrieveUpdateDestroyAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "Booking data deleted."}, status=status.HTTP_200_OK)


@permission_classes([IsAuthenticated])
class BookingByDate(ListAPIView):
    serializer_class = BookingSerializer

    def get_queryset(self):
        reservation_date = self.request.query_params.get('date', None)
        if reservation_date:
            reservation_query = Booking.objects.filter(reservation_date=reservation_date)
            return reservation_query
        else:
            return Booking.objects.all()


@permission_classes([IsAuthenticated])
class BookingItems(ListCreateAPIView):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def get_queryset(self):
        return Booking.objects.all()

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            reservation_exists = (Booking.objects.all().filter(reservation_date=self.request.data['reservation_date'])
                                  .filter(reservation_slot=self.request.data['reservation_slot']).exists())

            if not reservation_exists:
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
