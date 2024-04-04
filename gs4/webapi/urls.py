from django.urls import path
from webapi import views

urlpatterns = [
    path("student/", views.StudentAPI.as_view()),
]
