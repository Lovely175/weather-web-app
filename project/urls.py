from django.contrib import admin
from django.urls import path
from project import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<city_name>/',views.delete,name='delete'),

]