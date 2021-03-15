from rest_framework import serializers
from .models import Products
from django.core.exceptions import ValidationError
from profileapp.models import Client, Order, Subject
from django.db.models import OuterRef, Subquery, Sum



class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = ('id','name','cost','amount')

    def save(self):
        super(ProductSerializer, self).save()



class ProductDetailSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer(read_only=True,many=False)

    class Meta:
        model = Products
        fields = ('id', 'name', 'subjects','cost','amount')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','product','amount','created')

    def create(self,validated_data):
        product = validated_data['product']
        amount = validated_data['amount']
        price = Products.objects.filter(id=product.pk).first().cost
        total_price = price * amount
        order = Order.objects.create(product=product,amount=amount,total_price=total_price)
        return order


class ClientOrderCalculationSerializer(serializers.ModelSerializer):
    order_total_price = serializers.IntegerField()
    num_of_orders = serializers.IntegerField()
    class Meta:
        model = Client
        fields = [
            'id', 
            'name', 
            'order_total_price',
            'num_of_orders'
        ]
    
    
class ProductCalculationSerializer(serializers.ModelSerializer):
    total_cost = serializers.IntegerField()
    num_of_subject = serializers.IntegerField()

    class Meta:
        model = Subject
        fields = [
            'id',
            'name',           
            'total_cost',
            'num_of_subject'
        ]
  