from django.urls import path, include
from rest_framework import routers

from .views import (
    BlogArticleViewSet,
    FeedbackViewSet,
    WorkExampleViewSet,
    ServiceViewSet,
    FAQuestionViewSet,
    CompanyInfoView
)

router = routers.DefaultRouter()

router.register('blog', BlogArticleViewSet)
router.register('feedback', FeedbackViewSet)
router.register('work_example', WorkExampleViewSet)
router.register('service', ServiceViewSet)
router.register('faq', FAQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('company_info/', CompanyInfoView.as_view())
]
