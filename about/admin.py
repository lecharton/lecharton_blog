from django.contrib import admin

from .models import (
    Links, AdditionalLinks
)


class LinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_pub')
    search_fields = ('title', 'url')
    filter = ('is_pub',)


class AdditionalLinksAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_pub')
    search_fields = ('title', 'url')
    filter = ('is_pub',)


admin.site.register(Links, LinksAdmin)
admin.site.register(AdditionalLinks, AdditionalLinksAdmin)