from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name="index" ),
    path('test01',views.test01 ,name="test01" ),  
    path('test02',views.test02 ,name="test02" )   
]