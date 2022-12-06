from django.db import models
from django.forms import CharField
from django.db.models import CharField, IntegerField, FileField, ForeignKey, TextField, DateField, BooleanField, \
    EmailField, FloatField


class Customer(models.Model):
    customer_name = CharField(max_length=255)
    customer_number = CharField(max_length=255)
    customer_address = CharField(max_length=255)
    customer_added = DateField()

    def __str__(self):
        return f"{self.customer_name}, {self.customer_number}, {self.customer_address}"

class Challan(models.Model):
    challan_id = CharField(max_length=255)
    challan_date = DateField()
    delivery_date = DateField()
    delivery_type = CharField(max_length=20)
    customer = ForeignKey(Customer, on_delete=models.CASCADE)
    challan_delivery_status = CharField(max_length=20)

    def __str__(self):
        return f"{self.challan_id}, {self.challan_date}, {self.customer.id}"

class Tracker(models.Model):
    challan = ForeignKey(Challan, on_delete=models.CASCADE)
    tracker_status = CharField(max_length=20)

    def __str__(self):
        return f"{self.id},{self.challan.id},{self.tracker_status}"

class Iteam(models.Model):
    name = CharField(max_length=20)
    price = IntegerField()

    def __str__(self):
        return f"{self.id},{self.name},{self.price}"

class Service(models.Model):
    name = CharField(max_length=20)

    def __str__(self):
        return f"{self.id},{self.name}"