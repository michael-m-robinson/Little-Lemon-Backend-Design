# define URL route for index() view
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('restaurant/about/', views.about, name="about"),
    path('restaurant/book/', views.book, name="book"),
    path('restaurant/register/', views.register, name="register"),
    path('restaurant/login/', views.login_view, name="login"),
    path('restaurant/logout/', views.logout_view, name='logout'),
    path('restaurant/reservations/', views.reservations, name="reservations"),
    path('restaurant/menu/', views.menu, name="menu"),
    path('api/menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('api/bookings/', views.Bookings.as_view()),
    path('api/menu-items/', views.MenuItemView.as_view()),
    path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('401/', views.custom_401, name='custom_401'),
]
