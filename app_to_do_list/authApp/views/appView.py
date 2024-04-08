import os

from django.conf import settings
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse, HttpResponse, FileResponse, HttpResponseNotFound

from authApp.models.projects import  Project

from authApp.serializers.projectsSerializer import ProjectsSerializer


def show_projects(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return JsonResponse([ProjectsSerializer(project).data for project in projects], status=200, safe=False)
