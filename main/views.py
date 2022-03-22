from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import BlogArticle, FeedbackContact, WorkExample
from .serializers import (
    BlogArticleListSerializer,
    BlogDetailSerializer,
    FeedbackSerializer,
    WorkExampleDetailSerializer,
    WorkExampleListSerializer
)
from .pagination import WorkExamplesPagination


@method_decorator(csrf_exempt, name='dispatch')
class BlogArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BlogArticle.objects.all().order_by('-created')

    def get_serializer_class(self):
        if self.action == 'list':
            return BlogArticleListSerializer

        return BlogDetailSerializer


@method_decorator(csrf_exempt, name='dispatch')
class FeedbackViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FeedbackContact.objects.all()
    serializer_class = FeedbackSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


@method_decorator(csrf_exempt, name='dispatch')
class WorkExampleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = WorkExample.objects.all().order_by('-created')
    pagination_class = WorkExamplesPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkExampleListSerializer

        return WorkExampleDetailSerializer

