from django.contrib.auth.models import User
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    total_cost = models.FloatField()

class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    total_cost = models.FloatField()


    def __str__(self):
        return f'{self.product.name} - {self.quantity}'
