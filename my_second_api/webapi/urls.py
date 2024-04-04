from django.urls import path

from webapi import views

urlpatterns = [
    path('stucreate/', views.student_create),
    ]