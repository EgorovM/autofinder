from django.urls import path, include
from rest_framework import routers

from .views import BlogArticleViewSet, FeedbackViewSet, WorkExampleViewSet

router = routers.DefaultRouter()
router.register('blog', BlogArticleViewSet)
router.register('feedback', FeedbackViewSet)
router.register('work_example', WorkExampleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
