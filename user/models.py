from django.db import models
from django.contrib.auth.models import AbstractUser 

from user.custom_manager import UserManager 



class CustomUser(AbstractUser):


    # Since we use email as user name field , so we set username as None 
    username=None 

    email = models.EmailField(unique=True,max_length=100)
    phone_number = models.CharField(max_length=20,null=True)
    address=models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD='email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return f'email : {self.email}'
