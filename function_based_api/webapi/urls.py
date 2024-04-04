from django.urls import path
from webapi import views
urlpatterns = [
    path('studentapi/', views.student_api),
]
