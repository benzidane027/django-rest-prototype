from django.urls import path 
from . import views

urlpatterns = [
    path('to_do',views.index,name="index" ),  
]