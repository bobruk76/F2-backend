import jwt
from django.conf.global_settings import SECRET_KEY
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Question, Questionnaire
from .serializers import QuestionSerializer, QuestionnaireSerializer
from rest_framework import generics
from rest_framework.views import APIView


class QuestionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionnaireView(generics.ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer


class TestingView(APIView):
    def post(self, request):
        user = request.user

        result = request.data.get("answers")
        answers = json.loads(result)

        return Response({"success": "Request created successfully"})
