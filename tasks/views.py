from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from .utils import TaskPagination
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class TaskListCreatView(ListCreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'due_date']

    def get_queryset(self):
        # this ensures users only see their tasks
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # associate the task with the logged-in user
        serializer.save(user=self.request.user)


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination

    def get_queryset(self):
        # this ensures users only see their tasks
        return Task.objects.filter(user=self.request.user)
    

