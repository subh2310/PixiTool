from django.urls import path
from webapi import views
urlpatterns = [
    path('studentapi/', views.StudentAPI.as_view()),
    path('studentapi/<int:pk>/', views.StudentAPI.as_view()),
]