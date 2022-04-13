import imp
from django.shortcuts import render
from rest_framework import generics
from .models import *
from . serializers import *

# Create your views here.
class StidentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student
    serializer_class = StudentSerializer