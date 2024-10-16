from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Source(models.Model):
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Group(models.Model):
    date = models.DateField(auto_now_add=True)
    source = models.ForeignKey(Source,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_head = models.BooleanField(default=False)
    is_telecaller = models.BooleanField(default=False)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    mobile = models.CharField(max_length=15,null=True,blank=True)

    def __str__(self):
        return self.username