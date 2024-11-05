from django.urls import path
from .views import TodoItemViewSet

# 定義ViewSet的action
todo_list = TodoItemViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

todo_detail = TodoItemViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('todos/', todo_list, name='todo_list'),
    path('todos/<int:pk>/', todo_detail, name='todo_detail')
]