from django.urls import path
from . import views

urlpatterns = [
    path('todos/', views.ToDoList.as_view()),
    path('todos/<int:pk>/', views.ToDoDetail.as_view()),
]
