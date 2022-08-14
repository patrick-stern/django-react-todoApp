from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .pagination import CustomPagination
from rest_framework import status
from .serializers import TodoTaskSerializer
from .models import TodoTask
from .exceptions import NotFound


@api_view(['GET', 'POST'])
def taskList(request):

    if request.method == 'GET':
        paginator = CustomPagination()
        tasks = TodoTask.objects.all()
        context = paginator.paginate_queryset(tasks, request)
        serializer = TodoTaskSerializer(context, many = True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = TodoTaskSerializer(data=request.data)
         
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,  status=status.HTTP_201_CREATED)



@api_view(['GET', 'PATCH', 'DELETE'])
def taskDetail(request, id):

    try:
        task = TodoTask.objects.get(pk=id)
    except TodoTask.DoesNotExist:
        raise NotFound

    if request.method == 'GET':
        serializer = TodoTaskSerializer(task)
        return Response(serializer.data)


    if request.method == 'PATCH':
        serializer = TodoTaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_200_OK)


   
