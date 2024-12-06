from django.shortcuts import render
from .models import TaskModel
from .serializers import TaskSerializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@api_view(['GET', 'POST'])
def tasks_list(request):
    if request.method == 'GET':
        tasks = TaskModel.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        print(tasks_serializer)
        return JsonResponse(tasks_serializer.data, safe=False)

    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def task_details(request,pk):

    try:
        task = TaskModel.objects.get(pk=pk)
    except TaskModel.DoesNotExist:
        return JsonResponse({'message':'Task does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return JsonResponse(task_serializer.data)
    elif request.method == 'PUT':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(task, data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data)
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'msg':'Task deleted successfully'},status=status.HTTP_204_NO_CONTENT)

