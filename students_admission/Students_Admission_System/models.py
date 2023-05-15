from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.urls import reverse

# Create your models here.
class Application(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    
    COURSES = (
    ('Computer Science ', 'Computer Science '),
    ('Information Technology ', 'Information Technology '),
    ('Electronics and Telecommunication ', 'Electronics and Telecommunication '),
    ('Business and accounting', 'Business and accounting'),
    ('public Admin', 'public Admin'),
    ('LAW', 'LAW'),
    )
    course = models.CharField(max_length=100, choices= COURSES)
    name = models.CharField(max_length=200) 
    GENDER = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender = models.CharField(max_length=10, choices=GENDER)
    email = models.CharField(max_length=200) 
    phone_no = models.CharField(max_length=200) 
    address = models.CharField(max_length=200) 
    nationality = models.CharField(max_length=250)
    student_profile = models.ImageField(upload_to="images") 
    a_level_result = models.FileField()
    o_level_result = models.FileField()
    ple_result = models.FileField()
    kindergaten = models.FileField(null=True)
    national_id = models.ImageField(upload_to="images", null=True)
    DOM =(
        ('Boys hostel A','Boys hostel A'),
        ('Boys hostel B','Boys hostel B'),
        ('Boys hostel C','Boys hostel C'),
        ('Girls hostel A','Girls hostel A'),
        ('Girls hostel B','Girls hostel B'),
        ('Girls hostel C','Girls hostel C')
    )
    dom = models.CharField(max_length=50, choices=DOM)
    STATUS = (
        ('Approved', 'Approved'),
        ('Pending', 'Pending'),
        ('Rejected', 'Rejected'),
    )
    Application_Status = models.TextField(max_length=100, choices=STATUS, default="Pending")
    message = models.TextField(max_length=100, default="", null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('users')

class Notice(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Detail(models.Model):
    title = models.ForeignKey(Notice, on_delete=models.CASCADE)
    notice = models.CharField(max_length=200)

    def __str__(self):
        return self.notice