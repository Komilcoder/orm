# from django.db import models
# from django.contrib.auth import get_user_model
# from django.utils.translation import ugettext_lazy as _
# from django.core.validators import (
#     MaxValueValidator,
#     MinValueValidator,
#     RegexValidator,
# )
# from django.contrib.auth.models import(
#     AbstractBaseUser,
#     PermissionsMixin,
#     BaseUserManager,
# )
# import os
# from uuid import uuid4
# from django.core.exceptions import ValidationError

# def get_image(instance,filename):
#     ext = str(filename).split('.')[-1]
#     filename = f'{uuid4()}{ext}'
#     return os.path.join('user/image/',filename)


# class UserManager(BaseUserManager):
#     def create_user(self,phone_number,passsword,**extra_fields):
#         if not phone_number:
#             raise ValidationError('Users must have phone number') 
#         user = self.model(phone_number=phone_number, **extra_fields)
#         user.set_password(passsword)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,phone_number,password=None,**extra_fields):
#         user = self.create_user(phone_number,password=password,**extra_fields)
#         user.is_staff= True
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user


# class User(PermissionsMixin,AbstractBaseUser):
#     phone_number = models.CharField(max_length=255,unique=True,validators=[RegexValidator(regex=r'^(\+?998)?([. \-])?((\d){2})([. \-])?(\d){3}([. \-])?(\d){2}([. \-])?(\d){2}$',
#                                                        message="Given phone number is not valid")])
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)

#     objects = UserManager()
#     USERNAME_FIELD='phone_number'

#     def __str__(self):
#         return '{}{}{}'.format(self.phone_number, self.first_name, self.last_name)
        
 
                                                                   
