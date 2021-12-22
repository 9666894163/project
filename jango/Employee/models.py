from django.db import models

# Create your models here.

class Employee(models.Model):
    empno = models.IntegerField(primary_key=True)
    empname =models.CharField(max_length=20)
    empsalary =models.IntegerField(null=False,blank=False)
    joining_date = models.DateField(null=True)
    
    def __str__(self):
        return self.empname