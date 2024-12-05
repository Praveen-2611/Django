from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
# Create your models here.



class UserProfileManager(BaseUserManager):
    def create_user(self,email,firstname,lastname,password=None):
        if not email:
            raise ValueError('email is required')
        nemail=self.normalize_email(email)
        user=self.model(email=nemail,first_name=firstname,last_name=lastname)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,first_name,last_name,password):
        n_user=self.create_user(email,first_name,last_name,password)
        n_user.is_staff=True
        n_user.is_superuser=True
        n_user.save()


class UserProfile(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=100,primary_key=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=UserProfileManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['first_name','last_name']

