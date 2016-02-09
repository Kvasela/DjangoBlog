from django.shortcuts import render, get_object_or_404
from django.http import request
from django.views.generic import ListView, DetailView
import logging

from .models import Article, Tag

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class IndexView(ListView):
    queryset = Article.objects.published()
    template_name = "index.html"
    # paginate_by = 2


class ArticleView(DetailView):
    model = Article
    template_name = "article.html"


class TagView(ListView):
    template_name = "articles_by_tag.html"

    def get_queryset(self):
        slug = self.kwargs['tag']
        tag = get_object_or_404(Tag, slug=slug)
        return Article.objects.filter(tags=tag.id)

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context