from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import (
    Post, Tag
)

class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title', )

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'pub_date', 'is_pub')
    search_fields = ('title', 'slug')
    filter = ('is_pub',)
    summernote_fields = ('text',)
    readonly_fields = ('add_date',)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)