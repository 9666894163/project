
from django.shortcuts import render
from django.http import HttpResponse

from .forms import EmpForm
from .models import Employee
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html')

def empDetails(request):

    emp = EmpForm()
    try:
        print(request.POST)
        if request.method == 'POST':
            '''eno = request.POST['no']
            ename = request.POST['name']
            salary = request.POST['salary']
            print('Creating object')
            emp = Employee.objects.create(
                empno=eno, empname=ename, salary=salary)

            print(emp)

            print(eno, ename, salary) '''

            obj = EmpForm(request.POST)

            if obj.is_valid():

                obj.save()

                messages.success(request, 'Successfully inserted')

    except Exception:
        messages.error(request, 'Something went wrong')
        messages.info(request, 'It is looking like primary key issue')

    return render(request,'empdetails.html',{'form':emp,})

def fetchData(request):

    #if request.method =='POST':

    if request.method == 'GET':
        return render(request,'search.html')

    elif 'all' in request.POST:

        
        data = Employee.objects.all()

        context = {
            'info': data
        }

        return render(request,'output.html',context)
    else:
        eno = request.POST['sno']
        data = Employee.objects.filter(empno = eno)

        context = {
            'info': data
        }

        print(context)
        return render(request, 'output.html', context)
        
    

def deleteEmp(request):

    no = request.POST['eno']

    Employee.objects.filter(empno=no).delete()
 
    return render(request, 'empdetails.html')

    
    





