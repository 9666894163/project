
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EmpForm,CreateUser
from .models import Employee
from django.contrib import messages

# Create your views here.

def register(request):
    form = CreateUser()
    context = {'userform': form}
    if request.method =='POST':
        obj = CreateUser(request.POST)
        print(request.POST)
        if obj.is_valid():
            obj.save()
            return render(request,'login.html')
        else:
            print('form is not valid')
            print(obj.errors)
            return render(request,'register.html',context)

    
    return render(request,'register.html',context)            

@login_required(login_url='login')

def home(request):
    print(dir(request.session))

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

            #obj = EmpForm(request.POST)

            #if obj.is_valid():

                #obj.save()

                #messages.success(request, 'Successfully inserted')

            eForm = EmpForm(request.POST)

            if eForm.is_valid():
                emp = Employee()
                emp.empno = eForm.cleaned_data['empno']
                emp.empname = eForm.cleaned_data['empname']
                emp.salary = eForm.cleaned_data['salary']
                emp.joining_date = eForm.cleaned_data['joining_date']

                emp.save()
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

    if request.method == 'POST':

        no = request.POST['eno']

        Employee.objects.filter(empno=no).delete()
 
    return render(request, 'delete.html')


def userLogin(request):
    if request.method == 'POST':

        user = request.POST['user']
        pwd = request.POST['pwd']

        valid = authenticate(request,username = user,password = pwd )
        print(valid)
        
        if valid is not None:
            login(request,valid)
            request.session['username'] = user
            return render(request,'home.html')

        else:
            
            return render(request,'login.html')    



    return render(request,'login.html')


@login_required(login_url='login')
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request,'login.html')

    else:
        return render(request,'home.html')    
