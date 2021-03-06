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
    paginate_by = 5 


class ArticleView(DetailView):
    model = Article
    template_name = "article.html"


class TagView(ListView):
    template_name = "articles_by_tag.html"
    paginate_by = 5

    def get_queryset(self):
        slug = self.kwargs['tag']
        tag = get_object_or_404(Tag, slug=slug)
        return Article.objects.filter(tags=tag.id, publish=True)

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context


class SearchView(ListView):
    template_name = "search.html"
    paginate_by = 5

    def get_queryset(self):
        q = self.request.GET.get('q', None)
        return Article.objects.filter(title__icontains=q)

    def get_context_data(self, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['q'] = q = self.request.GET.get('q', None)
        return context
