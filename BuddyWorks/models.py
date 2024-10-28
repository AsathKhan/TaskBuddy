from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    ]
    
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    role= models.CharField(max_length=50, choices=ROLE_CHOICES, default="customer")
    
    def __str__(self):
        return self.user.username