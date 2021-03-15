# from rest_framework.fields import IntegerField
# from rest_framework.serializers import (
#     ModelSerializer,
#     Serializer,
#     CharField,
# )
# from django.core.validators import ValidationError
# from django.conf import settings
# from django.contrib.auth import get_user_model
# import pyotp
# import jwt
# import random

# from .models import User
# from .utils import is_phone_number_valid,generate_correct_number


# class UserCreateSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('first_name','last_name','password','phone_number')

#         read_only_fields = ('id')

#         extra_kwargs = {
#             'password':{
#                 'write_only':True,
#                 'min_length':5,
#                 'style':{
#                     'input_type':'password'
#                 }
#             }
#         }
#     def create(self,validated_data):
#         phone_number = validated_data['phone_number']
#         valid,msg = is_phone_number_valid(phone_number)

#         if not valid:
#             raise ValidationError(msg)
#         user = get_user_model().objects.filter(phone_number=phone_number)
#         if user:
#             raise ValidationError('A user with the given phone number already exists')
#         user = get_user_model().objects.create_user(**validated_data)
#         return user


# class UserSubSerializer(ModelSerializer):
#     class Meta:
#         model = User
#         fields = ("id", "first_name", "last_name",
#                   "phone_number", "paid_courses")



# class MainPasswordSerializer(Serializer):
#     @staticmethod
#     def validate_phone_number_exists(phone_number):
#         user = get_user_model().objects.filter(phone_number=phone_number).first()
#         if not user:
#             raise ValidationError('Given number was not found')
#         return user

# class CodeSendSerializer(MainPasswordSerializer):
#     phone_number = CharField(max_length=255)

#     def validate(self,attrs):
#         phone_number = attrs.get('phone_number')
#         valid,msg = is_phone_number_valid(phone_number)
#         if not valid:
#             raise ValidationError(msg)
#         self.validate_phone_number_exists(phone_number)
#         phone_number = generate_correct_phone_number(phone_number)
#         attrs['phone_number'] = phone_number
#         return attrs

#     @staticmethod
#     def validate_phone_number_exists(phone_number):
#         user_qa = get_user_model().objects.filter(phone_number=phone_number)
#         if user_qa:
#             raise ValidationError('This number is already exists')
        

# class CodeCheckSerializer(Serializer):
#     code = CharField(max_length=255)
#     phone_number = CharField(max_length=255)

#     def validate(self,attrs):
#         code = attrs.get('code',None)
#         phone_number = attrs.get('phone_number',None)
#         if not code or not phone_number:
#             raise ValidationError('Code or phone number is required')
#         valid,msg = is_phone_number_valid(phone_number)
#         if not valid:
#             raise ValidationError(msg)
#         self.validate_otp_code(code)
#         return attrs

#     @staticmethod
#     def validate_otp_code(code):
#         totp = pyotp.TOTP(settings.OTP_SECRET_KEY,interval=120)
#         res = totp.verify(code,valid_window=3)
#         if res is False:
#             raise ValidationError('code did not match')
#         return True


# class PasswordResetSerializer(MainPasswordSerializer):
#     token = CharField(write_only=True)
#     phone_number = CharField(write_only=True,max_length=255)
#     password = CharField(write_only=True,max_length=255)

#     def validate(self,attrs):
#         token = attrs.get('token')
#         phone_number = attrs.get('phone_number')
#         password = attrs.get('password')

#         if not phone_number or not token or not password:
#             raise ValidationError('Token phone number or password are required')
#         if len(password) < 5:
#             raise ValidationError('Password must be at least 5 characters')
#         valid,msg = is_phone_number_valid(phone_number)
#         if not valid:
#             raise ValidationError('Phone number is not valid')
#         user = self.validate_phone_number_exists(phone_number)
#         c_p = generate_correct_phone_number(msg)
#         self.validate_custom_token(token,c_p)
#         self.save_user_password(user,password)
#         return attrs

#     @staticmethod
#     def save_user_password(user,password):
#         user.set_password(password)
#         user.save() 


#     @staticmethod
#     def validate_custom_token(token,email):
#         if not token:
#             raise ValueError('Token is required')
#         try:
#             payload = jwt.deocde(token,settings.OTP_SECRET_KEY,algorithms=['HS256'])
#         except Exception as e:
#             raise ValidationError(str(e))
#         if payload.get('new_user') !=email:
#             raise ValidationError('payload did not match')
#         return token


# class PasswordCodeSerializer(MainPasswordSerializer):
#     phone_number = CharField(max_length=255)

#     def validate(self,attrs):
#         phone_number = attrs.get('phone_number')
#         valid,msg = is_phone_number_valid(phone_number)
#         if not valid:
#             raise ValidationError('phone number is not valid')
#         self.validate_phone_number_exists(msg)
#         c_p = generate_correct_number(msg)
#         attrs['phone_number'] = c_p
#         return attrs

        
