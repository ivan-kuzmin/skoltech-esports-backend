from rest_framework import viewsets
from .serializers import *


class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticlePreviewSerializer
        return ArticleDetailSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        return UserSerializer
