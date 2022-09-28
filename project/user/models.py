from pickle import TRUE

from django.db import models

class operation_theater(models.Model):
    username = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True,null=True)
    time = models.TimeField(auto_now_add=True,null=True)
    room = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.username


