from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'article', 'slug')
         }),
        ('Короткий зміст статті', {
            'classes': ('collapse',),
            'fields': ('excerpt',),
         }),
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_filter = ("publish", "modified")

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)