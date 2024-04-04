from django.urls import path
from webapi.views import LinuxCommandView

urlpatterns = [
    path('execute-command/', LinuxCommandView.as_view(), name='execute_command'),
]