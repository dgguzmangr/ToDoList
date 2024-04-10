from django.db import models
from django.utils import timezone


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField('Title', max_length=30)
    description = models.CharField('Description', max_length=400)
    creation_date = models.DateField('CreationDate', default=timezone.now)
    expiration_date = models.DateTimeField('ExpirationDate', null=True, blank=True)

    class Meta:
        app_label = 'authApp'