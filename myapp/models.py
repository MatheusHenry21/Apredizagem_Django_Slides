from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=11)

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_value = models.DecimalField(max_digits=10, decimal_places=2)