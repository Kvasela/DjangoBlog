from django.db import models


class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Тег")

    class Meta:
        verbose_name="тег"
        verbose_name_plural="теги"

    def __str__(self):
        return self.slug


class ArticleQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="заголовок")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="посилання")
    excerpt = models.TextField(verbose_name="коротикий зміст статті")
    article = models.TextField(verbose_name="повний зміст статті")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True, verbose_name="опублікована")
    tags = models.ManyToManyField(Tag, verbose_name="теги")

    objects = ArticleQuerySet.as_manager()

    class Meta:
        verbose_name = "статтю блогу"
        verbose_name_plural = "статті блогу"

    def __str__(self):
        return self.title