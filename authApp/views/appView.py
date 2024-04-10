from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from authApp.models.projects import Projects
from authApp.serializers.projectsSerializer import ProjectsSerializer
from authApp.models.tasks import Tasks
from authApp.serializers.tasksSerializer import TasksSerializer
from authApp.models.subTasks import SubTasks
from authApp.serializers.subTasksSerializer import SubTasksSerializer


# projects API

@api_view(['GET'])
def show_projects(request):
    if request.method == 'GET':
        projects = Projects.objects.all()
        serializer = ProjectsSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':
        serializer = ProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_project(request, pk):
    try:
        project = Projects.objects.get(pk=pk)
    except Projects.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = ProjectsSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_project(request, pk):
    try:
        project = Projects.objects.get(pk=pk)
    except Projects.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# tasks API

@api_view(['GET'])
def show_tasks(request):
    if request.method == 'GET':
        tasks = Tasks.objects.all()
        serializer = TasksSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_task(request):
    if request.method == 'POST':
        serializer = TasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_task(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TasksSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_task(request, pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# subtasks API

@api_view(['GET'])
def show_subtasks(request):
    if request.method == 'GET':
        subTasks = SubTasks.objects.all()
        serializer = SubTasksSerializer(subTasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_subtask(request):
    if request.method == 'POST':
        serializer = SubTasksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_subtask(request, pk):
    try:
        subTask = SubTasks.objects.get(pk=pk)
    except SubTasks.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = SubTasks(subTask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_subtask(request, pk):
    try:
        subTask = SubTasks.objects.get(pk=pk)
    except Tasks.DoesNotExist:
        return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        subTask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
