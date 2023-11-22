from django.urls import path

from maya.views import *
 
app_name='maya'

urlpatterns=[
 path('m/',m,name='m'),
]