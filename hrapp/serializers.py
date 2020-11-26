
from rest_framework import serializers
from django.contrib.auth.models import User
from hrapp.models import Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['content']

# from app.models import Post, Category
# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username']
#
#
# class PostSerializer(serializers.ModelSerializer):
#     author = AuthorSerializer(required=False)
#
#     category = serializers.StringRelatedField(many=True)
#
#
#     class Meta:
#         model = Post
#         fields = ['title','status','content','updated','publication_date', 'author','category']
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     posts = serializers.StringRelatedField(many=True)
#
#     class Meta:
#         model = Category
#         fields = ['name','posts']

