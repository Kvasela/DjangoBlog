from django.conf.urls import url
from django.conf.urls.static import static

from .views import IndexView, ArticleView, TagView, SearchView


urlpatterns = [
    url(r'^$', IndexView.as_view(), name="home"),
    url(r'^search/?$', SearchView.as_view(), name="search"),
    url(r'^article/(?P<slug>\S+)$', ArticleView.as_view(), name="article"),
    url(r'^tag/(?P<tag>\S+)$', TagView.as_view(), name="tag"),
]