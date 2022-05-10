from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    author = serializers.StringRelatedField()

    class Meta:
        madel = Article
        fields = '__all__'

# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     description = serializers.CharField()
#     slug = serializers.SlugField(max_length=200)
#     published = serializers.DateTimeField(read_only=True)
#
#     def create(self, validate_date):
#         return Article.objects.create(**validate_date)
#
#     def update(self, instance, validate_date):
#         instance.title = validate_date.get('title', instance.title)
#         instance.description = validate_date.get('description', instance.description)
#         instance.slug = validate_date.get('slug', instance.slug)
#         instance.published = validate_date.get('published', instance.published)
#         instance.save()
#         return instance
