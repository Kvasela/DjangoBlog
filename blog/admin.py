from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title',)
         }),
        ('Короткий зміст статті', {
            'classes': ('collapse',),
            'fields': ('excerpt',)
         }),
        (None, {
            'fields': ('article', 'slug', 'tags', 'publish',)
         }),
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_filter = ("publish", "created", "modified")

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)