from django.shortcuts import render
from django.http import HttpResponse
from webapi.models import Student
from webapi.serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer

def student_api(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializers(student)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def student_list_api(request):
    student = Student.objects.all()
    serializer = StudentSerializers(student, many=True)
    print(serializer.data)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')