from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.http import HttpResponse
from .models import Emp, Dept
from django.db.models import Q
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Sum, Count, Max, Min



def Home(request):
        # result = Emp.objects.all()
    # result = Emp.objects.filter(empname__exact='Veeranji')
    # result = Emp.objects.filter(empname__startswith='R')
    # result = Emp.objects.filter(salary__gt=60000)  # select * from Emp where salary>60000;
    # result = Emp.objects.filter(salary__gt=60000)
    # result = Emp.objects.filter(empname__icontains='e')
    # result = Emp.objects.filter(
    #   Q(empname__startswith='R') | Q(salary__gt=40000))
    try:

        #result = Emp.objects.get(salary__gt=40000)
        #result = Emp.objects.exclude(empname__startswith='V')
        # print(result)
        # for i in result:
        #   print(i.empname, i.salary)

        #result = Emp.objects.aggregate(Max('salary'))
        # print(result)

        # Emp.objects.values('')
        #results = Emp.objects.filter(dept__deptname='Development')
        # print(results)

        results = Emp.objects.values('dept').annotate(Sum('salary'))
        print(results)

        # for i in results:
        #   print(i.empname, i.salary)
    except MultipleObjectsReturned:
        return HttpResponse('Something went wrong')
    return HttpResponse('I am dummy app')

    return render(request,'home.html')

# For Registration
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your data created successfully')
            return render(request,'login.html')
    else:
        form = UserCreationForm()
    return render(request, 'register.html',{'form':form})


#For Login


def login_user(request):
    if request.method == 'POST':
        A= request.POST['users']
        B= request.POST['pwd']
        OBJ=authenticate(request, username=A, password=B)
        if OBJ is not None:
            login(request, OBJ)
            return render(render,'home.html')
    else:
        return render(request, 'login.html')
         

def user_creation_form(request):
    A = Form_s()
    return render(request, 'home.html', {'A':A})