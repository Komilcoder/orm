# from django.shortcuts import render
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.exceptions import NotFound
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser
# from rest_framework.generics import RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,ListCreateAPIView
# from rest_framework.viewsets import ModelViewSet
# from django.conf import settings
# from .models import User
# from .serializers import (
#     MainPasswordSerializer,
#     CodeSendSerializer,
#     CodeCheckSerializer,
#     UserCreateSerializer,
#     UserListSerializer,
#     PasswordResetSerializer,
#     PasswordCodeSerializer,
#     UserSubSerializer

# )    
# from .utils import send_code_phone_number,generate_correct_number,is_phone_number_valid
# import pyotp,jwt,random
# from django.contrib.auth import get_user_model



# def generate_otp():
#     totp = pytop.TOTP(settings.OTP_SECRET_KEY,interval=120)
#     code = totp.now()
#     return code


# """ User profile api """

# class UserProfileApiView(APIView):
#     permission_classes = [IsAuthenticated,]

#     def get(self,request,*args,**kwargs):
#         user = self.request.user.id
#         obj = User.objects.filter(id=user).first()
#         if not obj:
#             return Response({"user":"User not found"},status=status.HTTP_400_BAD_REQUEST)
#         serializer = UserSubSerializer(obj)
#         return Response({"user":serializer.data},status=status.HTTP_200_OK) 


#     def patch(self,request,*args,**kwargs):

#         user = request.user.id 
#         obj = User.objects.filter(id=user)
#         if not obj:
#             return Response({'error':'User not found'},status=status.HTTP_400_BAD_REQUEST)
#         first_name = request.data.get('first_name',None)
#         last_name = request.data.get('last_name',None)
#         if first_name is not None:
#             obj.first_name = first_name
#         if last_name is not None:
#             obj.last_name = last_name
#         obj.save(update_fields=['first_name','last_name'])
#         return Response({'user':UserSubSerializer(obj).data},status=status.HTTP_200_OK)



# """  sending code to phone number """

# class CodeSendApiView(APIView):

#     permission_classes = [AllowAny,]

#     def post(self, request,*args,**kwargs):
#         serializer = CodeSendSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         code = generate_otp() 
#         phone_number = request.data.get('phone_number')

#         payload = {
#             "code": code,
#             "phone_number":phone_number,
#         }   
#         return Response(payload, status=status.HTTP_200_OK)


# """ code check  """

# class CodeCheckAPIView(APIView):


#     def post(self,request,*args,**kwargs):
#         serializer = CodeCheckSerializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#         phone_number = request.data.get('phone_number')
#         token = jwt.encode({
#             "new_user":phone_number,
#             "rand_number":random.random()

#         },settings.OTP_SECRET_KEY,algorithm='HS256')

#         return Response({"phone_number": phone_number,"token":token},status=status.HTTP_200_OK)


# """ create user """

# class UserPagePagination(PageNumberPagination):
#     page_size = 10

#     def genrate_response(self,request,query_set,serializer_obj):
#         try:
#             page_date = self.paginate_queryset(query_set,request)
#         except NotFound:
#             return Response({'errors':'No result found'},status=status.HTTP_400_BAD_REQUEST)
#         serializer_class = serializer_obj(page_date,many=True)
#         return self.getpaginated_response(serializer_class.data)




# """ user list """
# class UserListCreateAPIView(ListCreateAPIView):

#     queryset = get_user_model().objects.all().filter(is_superuser=False)
#     serializer_class = UserCreateSerializer
#     permission_classes = [AllowAny,]
#     pagination_class = UserPagePagination

#     def get_serializer_class(self):
#         if self.request.method == 'GET':
#             return UserListSerializer
#         if self.request.method == 'POST':
#             return UserCreateSerializer

#     def get_permissions(self):
#         if self.request.method == 'POST':
#             permission_classes = [AllowAny,]
#         else:
#             permission_classes = [IsAdminUser,]
#         return [permission() for permission in permission_classes]  

#     def post(self, request,*args,**kwargs):
#         data = request.data 
#         token = data.get('token',None)

#         if not token:
#             return Response({'error':'Make sure you have include token'},status=status.HTTP_400_BAD_REQUEST)
#         payload = jwt.decode(token,settings.OTP_SECRET_KEY, algorithms=['HS256'])
#         phone_number = data.get('phone_number')
#         valid,msg = is_phone_number_valid(phone_number)
#         if not valid:
#             return Response({'error':'Phone number is not valid'})
#         c_p = generate_correct_number(msg)
#         if payload.get('new_user') != c_p:
#             return Response({'error':'Payload did not match'})
#         serializer = UserCreateSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# """ password reset """

# class PasswordResetApiView(APIView):

#     permission_classes = [AllowAny,]

#     def post(self,request,*args,**kwargs):
#         data = request.data
#         serializer = PasswordResetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



# """ password code  """

# class PasswordCodeApiView(APIView):

#     permission_classes = [AllowAny,]

#     def post(self,request,*args,**kwargs):
#         data = request.data
#         serializer = PasswordCodeSerializer(data=data)
#         if not serializer.is_valid():
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#         phone_number = serializer.data.get('phone_number')
#         code = generate_otp()
#         res = send_code_phone_number(code,phone_number,reset=True)
#         payload = {
#             'phone_number':phone_number,
#             'code':code,
#         }    
#         return Response(payload,status=status.HTTP_200_OK)
    







                      



