from rest_framework import viewsets, mixins, views, permissions
from rest_framework.response import Response

from .models import (
    BlogArticle,
    FeedbackContact,
    WorkExample,
    Service,
    CompanyInfo,
    FAQuestion
)
from .serializers import (
    BlogArticleListSerializer,
    BlogDetailSerializer,
    FeedbackSerializer,
    WorkExampleListSerializer,
    ServiceSerializer,
    CompanyInfoSerializer,
    FAQuestionSerializer
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
    authentication_classes = ()
    permission_classes = ()


class WorkExampleViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = WorkExample.objects.all().order_by('-created')
    pagination_class = WorkExamplesPagination
    serializer_class = WorkExampleListSerializer


class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all().order_by('title')
    pagination_class = None
    serializer_class = ServiceSerializer


class FAQuestionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FAQuestion.objects.all().order_by('question')
    pagination_class = None
    serializer_class = FAQuestionSerializer


class CompanyInfoView(views.APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None):
        company_info = CompanyInfo.objects.last()
        serializer = CompanyInfoSerializer(company_info)
        return Response(serializer.data)
