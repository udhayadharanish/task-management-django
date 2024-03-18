from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('tasks/',views.taskPage , name='tasks'),
    path('addTask/',views.addTask,name='addTask'),
    path('task/<str:pk>',views.task,name = 'task'),
    path('updateTask/<str:pk>',views.updateTask,name='updateTask'),
    path('deleteTask/<str:pk>',views.deleteTask,name='deleteTask'),
    path('completed/<str:pk>',views.completed,name='completed'),
]