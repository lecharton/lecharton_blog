from django.contrib import admin

from .models import (
    Project
)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'is_pub')
    search_fields = ('title', 'slug')
    filter = ('is_pub',)


admin.site.register(Project, ProjectAdmin)