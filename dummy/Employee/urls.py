from django.urls import path
from . import views

urlpatterns = [
    path('home',views.Home, name='sweethome'),
    path('register', views.user_register,name='regina'),
    path('loginme' , views.login_user, name='lol'),
]
   

    

