from rest_framework import serializers 
from .models import ToDo 

class ToDoSerializer(serializers.ModelSerializer):  # Create a serializer for the ToDo model
    class Meta:
        model = ToDo  # Tell the serializer to use the ToDo model
        fields = ['id', 'title', 'description', 'completed']  # Specify the fields we want to include in the API
