from django.urls import path
from . import views
from .views import TodoItemViewSet

# 定義ViewSet的action
todo_list = TodoItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('', views.home, name='home'),
    path('todos/', todo_list, name='todo_list')
]