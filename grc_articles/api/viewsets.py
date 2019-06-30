from rest_framework import viewsets
from api.models import *
from api.serializers import *
from django.shortcuts import redirect
from django.conf import settings
from rest_framework.response import Response

class TypeViewSet(viewsets.ModelViewSet):
	queryset= Type.objects.all()
	print(queryset)
	serializer_class=TypeSerializer

class CategoryViewSet(viewsets.ModelViewSet):
	queryset= Category.objects.all()
	serializer_class=CategorySerializer




class ArticleViewSet(viewsets.ModelViewSet):
	queryset= Articles.objects.all()
	serializer_class=ArticleSerializer


	def create(self,request):
		title=request.data['title']
		summary=request.data['summary']
		description = request.data['description']
		cover = request.data['cover']
		typename = int(request.POST.get('type_name'))
		print(typename)
		category = request.data['category']
		article=Articles.objects.create(
            user=request.user,
            title=title,
            summary=summary,
            description=description,
            cover = cover,
            typename = Type.objects.get(id=typename),
            category =category)
		article.save()
		return Response("Done")
 