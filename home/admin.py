from django.contrib import admin

# Register your models here.
from .models import homeDB, projectsDB, constructionPicsDB, elevationPicsDB, interiorPicsDB, teamDB, blogDB, testimonialDB

admin.site.register(homeDB)
admin.site.register(projectsDB)
admin.site.register(constructionPicsDB)
admin.site.register(elevationPicsDB)
admin.site.register(interiorPicsDB)
admin.site.register(teamDB)
admin.site.register(blogDB)
admin.site.register(testimonialDB)