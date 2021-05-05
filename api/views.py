# from django.shortcuts import render
from django.http import Http404, HttpRequest

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def api_overview(request: HttpRequest) -> Response:

    api_urls = {
        "List" : "/task-list/",
        "Detail View" : "/task-detail/<str:pk>",
        "Create" : "/task-create",
        "Update" : "/task-update/",
        "Delete": "/task-delete/"
    }

    return Response(api_urls)


@api_view(['GET'])
def task_list_view(request: HttpRequest) -> Response:

    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def details_view(request: HttpRequest, id: str) -> Response:

    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404

    serializer = TaskSerializer(task, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_view(request: HttpRequest) -> Response:

    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_view(request: HttpRequest, id: str) -> Response:

    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404

    task.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def update_view(request: HttpRequest, id: str) -> Response:
    print(request.data)
    try:
        task = Task.objects.get(id=id)
    except Task.DoesNotExist:
        raise Http404

    serializer = TaskSerializer(task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

