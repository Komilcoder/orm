from rest_framework import serializers
from .models import Client,Product,Post,Persons
from django.core.exceptions import ValidationError
from .utils import is_email_valid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from orm.models import Order




# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id,username','is_staff','is_active','is_superuser')
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = [
            'id',
            'username',
            'is_active'
        ]

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','client','name','price')

class ClientSerializer(serializers.ModelSerializer):
    count = serializers.CharField(max_length=100)
    total_price = serializers.CharField(max_length=100)
    class Meta:
        model = Client
        fields = ('id','name','count','total_price')

    def create(self,validated_data):
        name = validated_data.get('name')
        count = validated_data.get('count')
        valid = Client.objects.create(name=name,count=count)
        valid.save()
        return valid

        
class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('id','title','publish','status')

    def create(self,validated_data):
        title = validated_data['title']
        status = validated_data['status']
        

        post = Post.objects.create(title=title,status=status)
        post.save()
        return post


class PostDetailSerializer(serializers.ModelSerializer):
    """ this is only GET method taking user's """

    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Post
        fields = ('id','user','title','status','publish')
    

   
class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Persons
        fields = ('id', 'name', 'last_name', 'year', 'age', 'user')
    

    def validate(self, attrs):
        check_person = Persons.objects.filter(name=attrs.get('name'))
        if check_person.exists():
            raise serializers.ValidationError('This name is already exists!')
        return attrs
    
    
    def create(self,validated_data):
        # user = self.context['request'].user
        user = validated_data['user']
        name = validated_data['name']
        last_name = validated_data['last_name'] 
        year = validated_data['year']
        age = validated_data['age']
        instance = Persons.objects.create(user=user, name=name, last_name=last_name,year=year, age=age)
        return instance
    

class PersonSubSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Persons
        fields = ('id', 'email','password')

    def validate(self,validated_data):
        email = validated_data['email']
        password = validated_data['password']

        if '@' not in email:
            raise ValidationError('Email has a problem, check it')
        return email

        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters')
        return password

    def create(self,validated_data):
        email = validated_data['email']
        valid,msg = is_email_valid(email)
        if not valid:
            raise ValidationError(msg)
        user = get_user_model().objects.filter(email=email)

        if user:
            raise ValidationError('Email already in exists')

        user = get_user_model().create_user(**validated_data)
        return user



            
class PersonDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)
    older = serializers.SerializerMethodField()

    class Meta:
        model = Persons
        fields = ('id', 'name', 'last_name', 'year', 'age', 'user', 'older')
    
    
    def get_older(self, instance):
        flag = False 
        if int(instance.age) > 40:
            flag = True
        return flag
            

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persons
        fields = ('id', 'name', 'last_name', 'year', 'age')


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','client','name','price')


class OrderSerializer(serializers.ModelSerializer):

    # user = UserSerializer(read_only=True,many=False)

    class Meta:
        model = Order
        fields = ('id','product','client','create_date','status','amount')

    def create(self,validated_data):
        # user = validated_data['user']

        product = validated_data['product']
        client = validated_data['client']
        amount = validated_data['amount']
        price = Product.objects.filter(id=product.pk).first().price
        total_price = amount * price        
        instance = Order.objects.create(product=product,total_price=total_price,client=client,amount=amount)
        return instance




class OrderDetailSerializer(serializers.ModelSerializer):
    client = PersonModelSerializer(read_only=True,many=False)
    product = ProductModelSerializer(read_only=True,many=False)
    p_s = serializers.SerializerMethodField()

    
    class Meta:
        model = Order
        fields = ('id','product','total_price','client','create_date','status','p_s')

    def get_p_s(self,instance):
        flag = False
        if instance.total_price > 15:
            flag= True
        return flag    




