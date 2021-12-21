from django.contrib import admin
from django.urls import path
from student_fbapp import views

urlpatterns = [
    path('', views.feedback),
]