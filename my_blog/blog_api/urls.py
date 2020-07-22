from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = DefaultRouter()
router.register(r'v1/blogs', views.BlogViewSet)
router.register(r'v1/blogs/(?P<blog_id>[0-9]+)', views.BlogViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'api/', include(router.urls)),
]
