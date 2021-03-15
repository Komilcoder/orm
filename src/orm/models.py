from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime

class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
        

class Product(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.client}{self.name}'

    @receiver(pre_save,sender=client,dispatch_uid="update_client_count")
    def update_client_count(self,sender, **kwargs):
        client = kwargs['instance']
        if client.pk:
            Client.objects.filter(pk=client.client_id).update(client_count=F('client_count')+1)

             

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE,null=True,blank=True)
    title = models.CharField(max_length=100)
    publish = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)

    # def save(self, *args, **kwargs):
    #     super(Post,self).save(*args, **kwargs)


    def __str__(self):
        return self.title


class Persons(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    age = models.CharField(max_length=60)
    email = models.EmailField(max_length=50,null=True)
    password = models.CharField(max_length=100,null=True)

    def __str__(self):
        return f'{self.name}{self.last_name}{self.age}'

    class Meta:
        verbose_name = 'person'
          
choices = (
    ('pending','Pending'),
    ('complete','Complete'),
)
class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    total_price = models.IntegerField()
    client = models.ForeignKey(Persons,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100,choices=choices,default='pending')
    amount = models.PositiveIntegerField(default=0,null=True)


    def __str__(self):
        return str(self.product)
