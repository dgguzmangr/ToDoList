from django.db import models


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100)
    last_name = models.CharField('LastName', max_length=100)

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.name)
    
    class Meta:
        app_label = 'authApp'