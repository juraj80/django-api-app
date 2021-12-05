from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'author', 'email']


# ** SHELL COMMANDS
# from api_web_dev.models import Article
# from api_web_dev.serializers import ArticleSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# a = Article(title="Article Title", author="Juraj Klucka", email="juraj.klucka@gmail.com")
# a.save()
# serializer = ArticleSerializer(a)
# serializer.data   # returns PY dictionary
# content = JSONRenderer().render(serializer.data)   # return JSON repre
# serializer = ArticleSerializer(Article.objects.all(), many=True)
# serializer.data

# ** ModelSerializer 
# serializer = ArticleSerializer()
# print(repr(serializer))
