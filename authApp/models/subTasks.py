from django.db import models

class SubTasks(models.Model):
    sub_task_id = models.AutoField(primary_key=True)
    name = models.CharField('Title', max_length=30)
    description = models.CharField('Description', max_length=400)
    creation_date = models.DateField('Date', null=True)

    class Meta:
        app_label = 'authApp'