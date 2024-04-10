from django.contrib import admin
from .models.projects import Projects
from .models.tasks import Tasks
from .models.subTasks import SubTasks

admin.site.register(Projects)
admin.site.register(Tasks)
admin.site.register(SubTasks)