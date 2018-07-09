from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotAcceptable

from .models import Order, Pizza, Customer
from .serializers import OrderSerializer, PizzaSerializer, CustomerSerializer


class CustomerOrderAPIView(APIView):
    def get(self, request, pk):
        orders = Order.objects.filter(customer=pk)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CustomerFinderAPIView(APIView):
    def post(self, request):
        customer_name = request.data.get('customer_name', None)
        if not customer_name:
            return Response({"customer_name": ["please enter the customer name"]},
                            status=status.HTTP_404_NOT_FOUND)

        customer_address = request.data.get('customer_address', None)
        if not customer_address:
            return Response({"customer_address": ["please enter the customer address"]},
                            status=status.HTTP_404_NOT_FOUND)

        customer = Customer.objects.filter(customer_name=customer_name, customer_address=customer_address).first()
        if customer:
            customer_serializer = CustomerSerializer(customer)
            return Response(customer_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"customer": ["No customer found match the entered information."]},
                            status=status.HTTP_204_NO_CONTENT)


class OrderAPIView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        customer_name = request.data.get('customer_name', None)
        if not customer_name:
            return Response({"customer_name": ["please enter the customer name"]},
                            status=status.HTTP_404_NOT_FOUND)

        customer_address = request.data.get('customer_address', None)
        if not customer_address:
            return Response({"customer_address": ["please enter the customer address"]},
                            status=status.HTTP_404_NOT_FOUND)

        customer = Customer.objects.filter(customer_name=customer_name, customer_address=customer_address).first()

        if not customer:
            customer_serializer = CustomerSerializer(data={"customer_name": customer_name,
                                                           "customer_address": customer_address})
            customer_serializer.is_valid(raise_exception=True)
            customer_serializer.save()

            customer = Customer.objects.filter(customer_name=customer_name, customer_address=customer_address).first()

        serializer = OrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, order=None):
        if not order:
            raise NotAcceptable("please enter the order id you want to update in url like /order/order-id/")
        order = get_object_or_404(Order, pk=order)

        customer_name = request.data.get('customer_name', None)
        if not customer_name:
            return Response({"customer_name": ["please enter the customer name"]},
                            status=status.HTTP_404_NOT_FOUND)

        customer_address = request.data.get('customer_address', None)
        if not customer_address:
            return Response({"customer_address": ["please enter the customer address"]},
                            status=status.HTTP_404_NOT_FOUND)

        customer = Customer.objects.filter(customer_name=customer_name, customer_address=customer_address).first()
        if not customer:
            customer_serializer = CustomerSerializer(data={"customer_name": customer_name,
                                                           "customer_address": customer_address})
            customer_serializer.is_valid(raise_exception=True)
            customer_serializer.save()

            customer = Customer.objects.filter(customer_name=customer_name, customer_address=customer_address).first()

        serializer = OrderSerializer(order, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(customer=customer)
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
