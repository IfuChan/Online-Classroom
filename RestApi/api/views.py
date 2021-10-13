from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import StudentSerializer
from .models import Student

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List': '/user-list/',
        'Detail view': '/user-detail/<int:id>',
        'Create': '/user-create/',
        'Update': '/user-update/<int:id>',
        'Delete': '/user-detail/<int:id>'
    }

    return Response(api_urls);

@api_view(['GET'])
def ShowAll(request):
    student=Student.objects.all()
    serializer=StudentSerializer(student, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ShowStudent(request, pk):
    student=Student.objects.get(id=pk)
    serializer=StudentSerializer(student, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateStudent(request):
    serializer=StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        data="Account Created"
    return Response(data)

@api_view(['POST'])
def UpdateStudent(request,pk):
    student=Student.objects.get(id=pk)
    serializer=StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def DeleteStudent(request, pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return Response('Student deleted successfully!')