from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthenticationModule(AbstractUser):
    
    def __str__(self):
        return self.username

class EmployeeModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ProductModel(models.Model):
    product_name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.product_name
    
class  StudentModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    roll_number = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    course = models.CharField(max_length=100, null=True, blank=True)
    semester = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name
    