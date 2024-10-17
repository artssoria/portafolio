from django.contrib import admin
from .models import Project
#Esto es necesario para poder ver los campos de fecha de creacion y actualización
class ProjectAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Project, ProjectAdmin)
