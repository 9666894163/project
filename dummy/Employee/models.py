from django.db import models
from django import forms
from django.forms import ModelForm
from django.forms.fields import CharField

# Create your models here.

class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=15)

    def __str__(self):
        return self.deptname


class Emp(models.Model):
    ch = [
        ('M','Male'),
        ('F','Female'),
    ]
    empno = models.IntegerField(primary_key=True)
    empname = models.CharField(max_length=20)
    gender = models.CharField(max_length=5,choices=ch)

    dept = models.ForeignKey(Dept,on_delete=models.CASCADE)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return self.empname


class norman_forms(models.Model):
    userno = models.IntegerField()
    username = models.CharField(max_length=20)

    def __str__(self):
        return self.username