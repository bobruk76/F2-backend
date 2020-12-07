import jwt
from django.conf.global_settings import SECRET_KEY
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Question
from .serializers import QuestionSerializer
from rest_framework import generics
from rest_framework.views import APIView


class QuestionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class TestingView(APIView):
    def post(self, request):
        user = request.user
        
        result = request.data.get("answers")
        answers = json.loads(result)

        # Create an article from the above data
        # serializer = ArticleSerializer(data=article)
        # if serializer.is_valid(raise_exception=True):
        #     article_saved = serializer.save()
        return Response({"success": "Request created successfully"})
