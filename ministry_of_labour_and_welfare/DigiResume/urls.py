from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('login/',login),
    path('loginqr/',loginQR, name = 'loginqr'),
    path('<str:code>/home/',home,name='home'),
    path('<str:code>/register/',register, name='register'),
    path('<str:code>/add_course/',add_course,name='add_course'),
    path('<str:code>/add_work/',add_work,name='add_work'),
    path('<str:code>/add_resign/',add_resign,name='add_resign'),
    path('<str:code>/activity/',activity,name='activity'),
    path("<str:uid>/view_details/",view_details,name='view_details')
]

