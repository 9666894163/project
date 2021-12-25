from django import forms
from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm,Form
from django.forms.widgets import Widget
from django.contrib.auth.models import User
from .models import Employee


class EmpForm(ModelForm):
    '''class Meta:
        model = Employee
        fields = ['empno','empname','empsalary','joining_date']'''

class EmpForm(Form):
    empno = forms.IntegerField()
    empname = forms.CharField(max_length=25)
    empsalary = forms.IntegerField()
    joining_date = forms.DateField(widget=forms.SelectDateWidget) 

class CreateUser(ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']     