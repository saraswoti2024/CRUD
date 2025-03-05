from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('form/',form,name="form"),
    path('edit/<int:id>',edit,name="edit"), 
    path('delete/<int:id>',delete,name="delete"),
    path('restore_all/',restore_all,name="restore_all"),
     path('delete_all/',delete_all,name="delete_all"),
    path('recycle/',recycle,name="recycle")
]
