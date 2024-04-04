from django.urls import path
from webapi import views
urlpatterns = [
    path('student_api/', views.StudentAPI.as_view()),
]
