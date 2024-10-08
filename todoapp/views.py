from django.shortcuts import render
from rest_framework import viewsets  # Import DRF's viewsets, which handle CRUD logic automatically
from .models import ToDo  
from .serializers import ToDoSerializer
# Create a viewset for our ToDo API
class ToDoViewSet(viewsets.ModelViewSet):  
    queryset = ToDo.objects.all()  
    serializer_class = ToDoSerializer  

