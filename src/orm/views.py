from django.shortcuts import render
from .serializers import (
    ProductSerializer,
    ClientSerializer,
    PostSerializer,
  
    PersonSerializer,
    PersonSubSerializer,
    OrderSerializer
)    
from .models import Product,Client,Post,Persons
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,CreateAPIView,ListCreateAPIView
from django.contrib.auth.models import User
from django.db.models import OuterRef, Subquery
from django.db.models.expressions import F
from django.db.models.aggregates import Count, Max
import random
from django.db.models import Q
from django.core.exceptions import ValidationError
from orm.serializers import OrderDetailSerializer, PersonDetailSerializer, PostDetailSerializer
from orm.models import Order
from django.http import Http404



class ClientListView(APIView):

    def get(self,request,format=None):
        data = []
        sum = 0
        for client in Client.objects.all():
            products = Product.objects.filter(client=client)
            for product in products:
                sum = sum + product.price   
            data.append({
                'id': client.id,
                'name': client.name,
                'count':len(products),
                'total_price': sum
                  
            })
        return Response(data)
    

        
class PostListView(APIView):
    
    def get(self,request,format=None):
        post = Post.objects.all()
        serializer = PostSerializer(post,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request,format=None):
        
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)    
   
     
class PostDetailView(APIView):

    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self,request,pk=None):
        query = self.get_object(pk)
        serializer = PostDetailSerializer(query,many=False)  
        return Response(serializer.data)


class PersonView(ListAPIView):
    queryset = Persons.objects.all()
    serializer_class = PersonSerializer

    def list(self,request):
        query = self.get_queryset()
        serializer = PersonSerializer(query,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)




class PersonSubView(APIView):

    def post(self,request,format=None):
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        if not email or not password:
            raise ValidationError('Email or Password must be provided')
        
        person = Persons.objects.filter(email=email,password=password).first()
        serializer = PersonSubSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    



class PersonListView(ListCreateAPIView):
    queryset = Persons.objects.all()
    serializer_class =  PersonSerializer

    def get(self,request, *args, **kwargs):
        query = self.get_queryset()
        serializer = PersonDetailSerializer(query,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request, *args, **kwargs):
        data = request.data
        serializer = PersonSerializer(data=data, context= {"request": request}) # context 
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    


class PersonDetailAPView(APIView):

    def get_object(self, pk):
        try:
            return Persons.objects.get(pk=pk)
        except Persons.DoesNotExist:
            raise 400
    def get(self,request, pk=None):
        query = self.get_object(pk)
        serializer = PersonDetailSerializer(query, many=False)
        return Response(serializer.data)

    
class OrderApiView(APIView):

    def get(self,request,format=None):
        order = Order.objects.all()
        serializer = OrderSerializer(order,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        data = request.data
        serializer = OrderSerializer(data=data,context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrderDetailView(APIView):

    def get_object(self,pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404    

    def get(self,request,pk,format=None):
        query = self.get_object(pk)
        serializer = OrderDetailSerializer(query,many=False)
        return Response(serializer.data)    


        
        
        