from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from main.documents import ArticleDocument
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend
from main.serializers import ArticleDocumentSerializer


class ArticleDocumentView(DocumentViewSet):
    document = ArticleDocument
    serializer_class = ArticleDocumentSerializer
    filter_backends = [
        SearchFilterBackend
    ]

    search_fields = ('title',)
