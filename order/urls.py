from django.urls import path

from . import views

urlpatterns = [
    path('customer/find/', views.CustomerFinderAPIView.as_view(), name="customer_find"),
    path('customer/<int:pk>/', views.CustomerOrderAPIView.as_view(), name="customer"),

    path('order/', views.OrderAPIView.as_view(), name="order"),
    path('order/<int:order>/', views.OrderAPIView.as_view(), name="order"),

    path('pizza/', views.PizzaAPIView.as_view(), name="pizza"),
    path('pizza/<int:pizza>/', views.PizzaAPIView.as_view(), name="pizza"),
]
