from rest_framework import serializers
from api.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=('id', 'username', 'first_name','last_name','email')


class TypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Type
		fields = ('id','type_name')
		depth=1

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ('id','category_name','category_image')
		depth=1


class ArticleSerializer(serializers.ModelSerializer):
	user = UserSerializer()
	typename = TypeSerializer()
	category = CategorySerializer()
	class Meta:
		model = Articles
		fields = ('id','title','summary','description','cover','user','typename','category')
		depth=1
