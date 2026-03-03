from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.TaskListCreatView.as_view(), name='task-list-create'),
    path('<int:pk>/', views.TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
]