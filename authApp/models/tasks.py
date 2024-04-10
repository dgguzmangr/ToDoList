from django.db import models
from .projects import Projects

class Tasks(models.Model):
    task_id = models.AutoField(primary_key=True)
    name = models.CharField('Title', max_length=30)
    description = models.CharField('Description', max_length=400)
    creation_date = models.DateField('Date', auto_now_add=True)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='tasks')

    class Meta:
        app_label = 'authApp'