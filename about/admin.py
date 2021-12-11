from django.contrib import admin

from .models import (
    Links, AdditionalLinks, Application
)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'type')
    search_fields = ('name', 'surname')
    filter = ('type',)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_pub')
    search_fields = ('title', 'url')
    filter = ('is_pub',)


class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_pub')
    search_fields = ('title', 'url')
    filter = ('is_pub',)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Links, LinksAdmin)
admin.site.register(AdditionalLinks, AdditionalLinksAdmin)