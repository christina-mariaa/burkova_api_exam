from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializators import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
