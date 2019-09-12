from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="HomePage"),
    path('delete/<str:list_id>', views.delete, name="DeleteItem"),
    path('crossoff/<str:list_id>', views.crossoff, name="Crossoff"),
    path('uncross/<str:list_id>', views.uncross, name="Uncross"),
    path('edit/<str:list_id>', views.edit, name="EditItem"),
]
