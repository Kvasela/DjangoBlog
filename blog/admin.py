from django.contrib import admin
from .models import Article, Tag


class ArticleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            "fields": ("title", "excerpt", "article", "slug", "tags", "publish",)
         }),
    )
    prepopulated_fields = {
        "slug": ("title",)
    }
    list_filter = ("publish", "created", "modified")
    list_display = ("title", "created", "modified")
    search_fields = ["title"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)