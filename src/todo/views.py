from django.shortcuts import render
from django.http import HttpResponse
from .models import TodoItem
from django.http import JsonResponse

# Create your views here.
def home(request):
    return HttpResponse('Hello, World!')

def todo_list(request):
    todos = TodoItem.objects.all().values()
    return JsonResponse({'todos': list(todos)}, safe=False)
    