from authApp.models.tasks import Tasks
from rest_framework import serializers


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['task_id', 'name', 'description', 'creation_date']