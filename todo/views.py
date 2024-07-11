from rest_framework import generics
from .models import ToDoItem
from .serializers import ToDoItemSerializer

class ToDoList(generics.ListCreateAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
