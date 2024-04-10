from django.db import models
from django.utils import timezone


class Projects(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField('Title', max_length=30)
    description = models.CharField('Description', max_length=400)
    creation_date = models.DateField('CreationDate', default=timezone.now)
    expiration_date = models.DateTimeField('ExpirationDate', null=True, blank=True)
    STATUS_CHOICES = [
        ('En espera', 'En espera'),
        ('En progreso', 'En progreso'),
        ('Finalizada', 'Finalizada'),
    ]
    status = models.CharField('Status', max_length=20, choices=STATUS_CHOICES)
    class Meta:
        app_label = 'authApp'