from django.db import models


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField('Title', max_length=30)
    description = models.CharField('Description', max_length=400)
    creation_date = models.DateField('Date', auto_now_add=True)

    class Meta:
        app_label = 'authApp'