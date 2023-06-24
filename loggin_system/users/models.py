from django.db import models

# Create your models here.
class Register(models.Model):
    ROLES_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
    )
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Country = models.CharField(max_length=20)
    Nationality = models.CharField(max_length=25)
    Mobile = models.IntegerField()
    Password = models.CharField(max_length=10)
    Roles = models.CharField(max_length=10, choices=ROLES_CHOICES)
