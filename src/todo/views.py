from .models import TodoItem
from rest_framework import viewsets
from .serializers import TodoItemSerializer

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    http_method_names = ['get', 'post', 'put','delete']


    