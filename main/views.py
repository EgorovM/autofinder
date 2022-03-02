from rest_framework import viewsets, mixins

from .models import BlogArticle, FeedbackContact, WorkExample
from .serializers import (
    BlogArticleListSerializer,
    BlogDetailSerializer,
    FeedbackSerializer,
    WorkExampleDetailSerializer,
    WorkExampleListSerializer
)
from .pagination import WorkExamplesPagination


class BlogArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogArticle.objects.all().order_by('-created')

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogArticleListSerializer

        return BlogDetailSerializer


class FeedbackViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FeedbackContact.objects.all()
    serializer_class = FeedbackSerializer


class WorkExampleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkExample.objects.all().order_by('-created')
    pagination_class = WorkExamplesPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkExampleListSerializer

        return WorkExampleDetailSerializer

