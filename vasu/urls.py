from django.urls import path

from vasu.views import *
 
app_name='vasundhara'

urlpatterns=[
 path('v/',v,name='v'),
]