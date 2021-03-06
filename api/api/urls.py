from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from .view import ArticleViewSet, CategoryViewSet

router = DefaultRouter()
router.register('article', ArticleViewSet, 'Article')
router.register('category', CategoryViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)