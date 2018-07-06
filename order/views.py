from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAcceptable

from .models import Order, Pizza
from .serializers import OrderSerializer, PizzaSerializer


class CustomerOrderAPIView(APIView):
    def get(self, request, customer):
        orders = Order.objects.filter(customer_name=customer)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, order=None):
        if not order:
            raise NotAcceptable("please enter the order id you want to update in url like /order/order-id/")
        order = get_object_or_404(Order, pk=order)
        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, order=None):
        if not order:
            raise NotAcceptable("please enter the order id you want to delete in url like /order/order-id/")
        order = get_object_or_404(Order, pk=order)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PizzaAPIView(APIView):
    def get(self, request):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PizzaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pizza=None):
        if not pizza:
            raise NotAcceptable("please enter the pizza id you want to update in url like /pizza/pizza-id/")
        order = get_object_or_404(Pizza, pk=pizza)
        serializer = PizzaSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pizza=None):
        if not pizza:
            raise NotAcceptable("please enter the pizza id you want to delete in url like /pizza/pizza-id/")
        order = get_object_or_404(Pizza, pk=pizza)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
