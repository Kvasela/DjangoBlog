from django.conf.urls import url
from .views import IndexView, ArticleView, TagView


urlpatterns = (
    url(r'^$', IndexView.as_view(), name="home"),
    url(r'^article/(?P<slug>\S+)$', ArticleView.as_view(), name="article"),
    url(r'^tag/(?P<tag>\S+)$', TagView.as_view(), name="tag"),
)