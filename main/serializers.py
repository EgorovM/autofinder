from rest_framework import serializers
from .models import BlogArticle, FeedbackContact, WorkExample


class BlogDetailSerializer(serializers.ModelSerializer):
    is_youtube = serializers.SerializerMethodField()
    asset = serializers.SerializerMethodField()

    class Meta:
        model = BlogArticle
        fields = ['id', 'title', 'content', 'created', 'is_youtube', 'asset']

    def get_is_youtube(self, obj: BlogArticle):
        return obj.youtube_id != ""

    def build_absolute_url(self, image_url: str):
        request = self.context.get('request')
        return request.build_absolute_uri(image_url)

    def get_asset(self, obj: BlogArticle):
        if self.get_is_youtube(obj):
            return 'https://www.youtube.com/watch?v=%s' % obj.youtube_id

        return self.build_absolute_url(obj.img.url)


class BlogArticleListSerializer(BlogDetailSerializer):
    content = serializers.SerializerMethodField()

    def get_content(self, obj):
        return obj.short_content()

    def get_asset(self, obj):
        if self.get_is_youtube(obj):
            return 'https://img.youtube.com/vi/%s/hqdefault.jpg' % obj.youtube_id

        return self.build_absolute_url(obj.img.url)


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackContact
        fields = '__all__'


class WorkExampleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExample
        fields = '__all__'
