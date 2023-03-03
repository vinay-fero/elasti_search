# urls.py
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from main.views import ArticleDocumentView

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'article-search', ArticleDocumentView, basename='article-search')
urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
