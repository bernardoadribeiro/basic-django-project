from django.contrib import admin
from projects.models import Project

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technology', 'description')
    list_filter = ('title', 'technology',)
    search_fields = ('title', 'technology')


admin.site.register(Project, ProjectAdmin)
