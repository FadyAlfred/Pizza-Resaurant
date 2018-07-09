from django.contrib import admin

from .models import Pizza, Order, Customer

admin.site.register(Pizza)
admin.site.register(Order)
admin.site.register(Customer)
