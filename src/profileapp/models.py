from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    client = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name




class Subject(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Products(models.Model):
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    cost = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    total_price = models.IntegerField()
    client = models.ForeignKey(Client,on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.product)

