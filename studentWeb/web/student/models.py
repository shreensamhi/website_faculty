from django.db import models
from django.forms import PasswordInput

# Create your models here.
class student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    GENDER_CHOICE = (
        ('A', 'Active'),
        ('I', 'Inactive'),
    )
    studentname = models.CharField(max_length=100)
    studentid = models.IntegerField(max_length=8)
    birthday = models.DateField()
    gpa = models.DecimalField(max_digits=3,decimal_places=2)
    level = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    email = models.EmailField(max_length=50)
    phonenumber = models.IntegerField(max_length=11)
    department = models.CharField(max_length=50)
    status = models.CharField(max_length=1, choices=GENDER_CHOICE, null=True)

    def __str__(self) -> str:
        return self.studentname
    class Meta:
        ordering=['studentname']


class Login(models.Model):
    username = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.username