from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer


# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

class TodoItemViewSet(viewsets.ModelViewSet):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer


    