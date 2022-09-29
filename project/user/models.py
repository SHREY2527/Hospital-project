from pickle import TRUE
from .views import Login,register
from django.contrib.auth.models import User


from django.db import models

class operation_theater(models.Model):
    Username = models.CharField(max_length=200,null=True)
    email =models.EmailField(max_length=200,null=True)
    date = models.DateField(max_length=50,null=True)
    time = models.TimeField(max_length=50,null=True)
    room = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.Username


