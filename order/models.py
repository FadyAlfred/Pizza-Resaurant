from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Pizza(TimeStampedModel):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)


class Customer(TimeStampedModel):
    customer_name = models.CharField(max_length=128)
    customer_address = models.TextField()


class Order(TimeStampedModel):
    SIZE_SMALL = 30
    SIZE_LARGE = 50

    SIZE_CHOICES = (
        (SIZE_SMALL, '30 cm'),
        (SIZE_LARGE, '50 cm'),
    )

    pizza_id = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="orders")
    pizza_size = models.CharField(max_length=2, choices=SIZE_CHOICES)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")

