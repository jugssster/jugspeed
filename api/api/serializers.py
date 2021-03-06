from rest_framework import serializers
from django.contrib.auth.models import User
from .model import Article, Category

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    author = UserDetailSerializer(read_only=True)
    category = CategoryDetailSerializer(read_only=True)
    class Meta:
        model = Article
        fields = '__all__'

