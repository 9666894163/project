from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name = 'home'),
    #path('',views.empDetails,name = 'empdetails'),
    path('input',views.empDetails,name = 'inputdata'),
    path('output',views.fetchData),
    path('delete_emp',views.deleteEmp),
   
]