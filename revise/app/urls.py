from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('form/',form,name="form"),
    path('edit/',edit,name="edit"),
    print('delete/<int:id>',delete,name="delete"),
]
