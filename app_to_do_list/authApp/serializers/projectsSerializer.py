from authApp.models.projects import Projects
from rest_framework import serializers


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['project_id', 'name', 'description', 'creation_date']