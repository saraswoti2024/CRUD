from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('form/',form,name="form"),
    path('edit/<int:id>',edit,name="edit"),
    path('delete/<int:id>',delete,name="delete"),
    path('recycle/',recycle,name="recycle")
]
