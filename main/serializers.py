import re
from rest_framework import serializers
from .models import (
    BlogArticle,
    FeedbackContact,
    WorkExample,
    Service,
    CompanyInfo,
    FAQuestion,
    Info
)


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
    additional_images = serializers.SerializerMethodField()

    class Meta:
        model = WorkExample
        exclude = WorkExample.ADDITIONAL_IMAGES_FIELDS

    def get_additional_images(self, obj):
        request = self.context.get('request')
        urls = []

        for img_field_name in WorkExample.ADDITIONAL_IMAGES_FIELDS:
            img_field = getattr(obj, img_field_name)

            try:
                urls.append(request.build_absolute_uri(img_field.url))
            except Exception as e:  # todo
                pass

        return urls


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class CompanyInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyInfo
        fields = '__all__'


class FAQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQuestion
        fields = '__all__'


class InfoSerializer(serializers.ModelSerializer):
    value = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['id', 'slug', 'value']

    def get_value(self, obj):
        value = obj.value

        value = re.sub('class="[^"]*"', '', value)
        value = re.sub('<(\w*) ', '<span ', value, 1)
        value = re.sub('</\w+>$', '</span>', value)

        return value
