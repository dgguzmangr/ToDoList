from django.contrib import admin
from .models.projects import Projects
from .models.tasks import Tasks
from .models.subTasks import SubTasks
from .models.persons import Person

admin.site.register(Projects)
admin.site.register(Tasks)
admin.site.register(SubTasks)
admin.site.register(Person)