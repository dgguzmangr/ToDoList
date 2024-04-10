from django.db import models
from .projects import Projects
from .tasks import Tasks

class SubTasks(models.Model):
    sub_task_id = models.AutoField(primary_key=True)
    name = models.CharField('Title', max_length=30)
    description = models.CharField('Description', max_length=400)
    creation_date = models.DateField('Date', auto_now_add=True)
    task_id = models.ForeignKey(Tasks, on_delete=models.CASCADE, related_name='subTasks')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE, related_name='subTasks')

    class Meta:
        app_label = 'authApp'