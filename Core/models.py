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

class FollowUp(models.Model):
    lead = models.ForeignKey(Lead,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=50)
    details = models.TextField(null=True,blank=True)

    def __str__(self):
        return f'{self.lead} / {self.title}'

class Booking(models.Model):
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=25,default='pending')

    lead = models.ForeignKey(Lead,on_delete=models.CASCADE)
    students = models.IntegerField()
    teachers = models.IntegerField()
    visit_date = models.DateField()

    time_arrival = models.TimeField(null=True,blank=True)
    time_leave = models.TimeField(null=True,blank=True)

    food = models.CharField(max_length=50,null=True,blank=True)
    info = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.lead.name