from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from main.documents import ArticleDocument


class ArticleDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ArticleDocument
        fields = (
            'title',
            'category'
        )
