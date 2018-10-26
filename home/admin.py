from django.contrib import admin

# Register your models here.
from .models import homeDB, projectsDB

admin.site.register(homeDB)
admin.site.register(projectsDB)
