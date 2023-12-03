# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("book/", views.book, name="book"),
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("reservations/", views.reservations, name="reservations"),
    path("menu/", views.menu, name="menu"),
    path("api/menu_item/<int:pk>/", views.display_menu_item, name="menu_item"),
    path("api/bookings/", views.BookingItems.as_view(), name="bookings"),
    path("api/booking_date/", views.BookingByDate.as_view(), name="booking_date"),
    path(
        "api/booking_item/<int:pk>/",
        views.SingleBookingItem.as_view(),
        name="booking_item",
    ),
    path("api/menu-items/", views.MenuItemView.as_view()),
    path("api/menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    path("401/", views.custom_401, name="custom_401"),
]
