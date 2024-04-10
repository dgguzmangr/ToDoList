from authApp.models.tasks import Tasks
from rest_framework import serializers


class SubTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['sub_task_id', 'name', 'description', 'creation_date']