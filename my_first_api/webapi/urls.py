from django.urls import path
from webapi import views

urlpatterns = [
    path("api/<int:pk>", views.student_api),
    path("api/",views.student_list_api ),
]
