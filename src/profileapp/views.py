from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Products,Order
from .serializers import ProductSerializer,OrderSerializer,ProductDetailSerializer
from profileapp.models import Client, Subject
from django.db.models import OuterRef, Subquery, Sum
from profileapp.serializers import ClientOrderCalculationSerializer, ProductCalculationSerializer
from django.db.models.aggregates import Count


class ProductListView(APIView):

    def get(self,request, *args, **kwargs):
        product = Products.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)

    def post(self,request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)   
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):

    def get(self,request,*args,**kwargs):
        order = Order.objects.all()
        serializer = OrderSerializer(order,many = True)
        return Response(serializer.data)

    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class ClientOrderCalculation(APIView):
    def get(self, request):
        clients = Client.objects.all()
        orders = Order.objects.filter(client=OuterRef('pk')).order_by('-created') #OuterRef key buyicha filter qib beradi xoxlagan narsa buyicha
        orders = orders.values(total_sum=Sum('total_price')) # values , bir nechta bulganlarni bitta qib beradi key buyicha
        orders = orders.order_by() # order qib quyish uchun
        orders.query.group_by = []
        clients = clients.annotate(order_total_price=Subquery(orders[:1])) # Subquery  2 ta tableni bog'layabdi ,client va order (Subquery(order))
        order_counts = orders.values(order_count=Count('pk'))
        order_counts = order_counts.order_by()
        order_counts.query.group_by = []
        clients = clients.annotate(num_of_orders=Subquery(order_counts[:1])) #annotate queryga yangi field qushib beradi
        serializer = ClientOrderCalculationSerializer(clients, many=True)
        return Response(serializer.data)

# Sum djangoda hisoblab beradi 
# Count sanab beradi       


class ProductOrderCalculation(APIView):

    def get(self,request):
        subjects = Subject.objects.all()
        product = Products.objects.filter(subject=OuterRef('pk'))
        product = product.values(total_cost=Sum('cost'))
        product = product.order_by()
        product.query.group_by = []
        subjects = subjects.annotate(total_cost=Subquery(product[:1]))
        number_count = product.values(number=Count('pk'))
        number_count= number_count.order_by()
        number_count.query.group_by = []
        subjects = subjects.annotate(num_of_subject=Subquery(number_count[:1]))
        serializer = ProductCalculationSerializer(subjects,many=True)
        return Response(serializer.data)
        


