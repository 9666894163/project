from django import forms
from django.db import models
from django.forms import ModelForm,Form
from django.forms.widgets import Widget

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

        