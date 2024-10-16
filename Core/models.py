from django.db import models
from Authentication.models import Source, Group, User

# Create your models here.

LEAD_STATUS = (
    ('HOT','HOT'),
    ('NORMAL','NORMAL'),
    ('COLD','COLD'),
    ('DEAD','DEAD'),
)

class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Lead(models.Model):
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,default='PENDING')
    lead_type = models.CharField(max_length=25,choices=LEAD_STATUS,default='NORMAL')
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    sub_district = models.CharField(max_length=50)
    departments = models.ManyToManyField(Department)
    students = models.IntegerField(null=True, blank=True)
    teachers = models.IntegerField(null=True, blank=True)
    primary_name = models.CharField(max_length=50,null=True,blank=True)
    primary_number = models.CharField(max_length=15,null=True,blank=True)
    secondary_name = models.CharField(max_length=50,null=True,blank=True)
    secondary_number = models.CharField(max_length=15,null=True,blank=True)
    source = models.ForeignKey(Source,on_delete=models.SET_NULL,null=True)
    group = models.ForeignKey(Group,on_delete=models.SET_NULL,null=True)
    staff = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
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