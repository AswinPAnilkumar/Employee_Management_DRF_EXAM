from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_name