from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Room(models.Model):
    name = models.CharField(max_length=200)
    places=models.IntegerField()
    free_places=models.IntegerField()
    order_a= models.TextField(null=True,blank=True)
    order_b= models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name


class Customer(models.Model):
    email = models.EmailField(max_length=200)
    time= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

