from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('login/',login),
    path('home/',home),
    path('register/',register),
    path('add_course/',add_course),
    path('add_work/',add_work),
    path('history/',history),
    path('activity/',activity),
    path('view_details/',view_details)
]
