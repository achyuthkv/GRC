from django.urls import path,include

from rest_framework.routers import DefaultRouter
from api.viewsets import *

router=DefaultRouter()
router.register(r'type',TypeViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'article',ArticleViewSet)


urlpatterns=[
	path('',include(router.urls))
]