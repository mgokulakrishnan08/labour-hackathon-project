from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('login/',login),
    path('<str:code>/home/',home),
    path('<str:code>/register/',register),
    path('<str:code>/add_course/',add_course),
    path('<str:code>/add_work/',add_work),
    path('<str:code>/history/',history),
    path('<str:code>/activity/',activity),
    path("<str:uid>/view_details/",view_details)
]

    # path("<str:uid>/view_details/",view_details)
