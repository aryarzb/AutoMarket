from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    state = models.CharField(max_length=50);
    city = models.CharField(max_length=50);
    mobile_number = PhoneNumberField(unique=True);
    address = models.TextField();
    
