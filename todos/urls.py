from django.urls import path
from .views import TodoList, TodoDetail, UserList, UserDetail

urlpatterns = [
    path('todo/', TodoList.as_view()),
    path('todo/<int:pk>/', TodoDetail.as_view()),
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view(),)
]
