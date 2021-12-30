from django import forms
from .models import *


class Form_s(forms.ModelForm):
    class Meta:
        model = norman_forms
        fields = '__all__'