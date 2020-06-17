from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   
    path('',views.index,name="index"),
    path('<int:order_id>/',views.orderdetails,name="orderdetails"),
]