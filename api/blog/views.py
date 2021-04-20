from rest_framework.status import *
from rest_framework import viewsets

from .models import Article, Category, Comment
from .serializers import *


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        # set query to default
        query = Article.objects.all()
        # pop 'limit' key before filter to prevent break
        params = self.request.query_params.dict()
        limit = params.pop('limit', None)
        if params:
            # filter objects based on query params
            query = Article.objects.filter(**params)
        if limit:
            # apply limit
            return query.order_by('-id')[0:int(limit)]
        # return without limit
        return query


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        # set query to default
        query = Comment.objects.all()
        # pop 'limit' key before filter to prevent break
        params = self.request.query_params.dict()
        limit = params.pop('limit', None)
        if params:
            # filter objects based on query params
            query = Comment.objects.filter(**params)
        if limit:
            # apply limit
            return query.order_by('-id')[0:int(limit)]
        # return without limit
        return query
    