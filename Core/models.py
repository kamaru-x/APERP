from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Lead(models.Model):
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,default='pending')
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    sub_district = models.CharField(max_length=50)
    departments = models.ManyToManyField('Department')
    students = models.IntegerField(null=True, blank=True)
    teachers = models.IntegerField(null=True, blank=True)
    contact_name = models.CharField(max_length=50,null=True,blank=True)
    contact_number = models.CharField(max_length=15,null=True,blank=True)
    info = models.TextField()

    def __str__(self):
        return self.name