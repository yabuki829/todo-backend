from django.contrib import admin
from django.urls import path, include
from .views.todo import TodoView,test



urlpatterns = [
    path('test/', test, name="test"),
    
]