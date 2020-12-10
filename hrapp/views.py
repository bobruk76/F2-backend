import jwt
from django.conf.global_settings import SECRET_KEY
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Question, Questionnaire
from .serializers import QuestionSerializer, QuestionnaireSerializer, QuestionnaireListSerializer
from rest_framework import generics, status
from rest_framework.views import APIView


class QuestionView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionnaireList(generics.ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireListSerializer


class QuestionnaireView(APIView):

    def get_object(self, pk):
        try:
            return Questionnaire.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request, pk, format=None):
        questionnaire = self.get_object(pk)
        serializer = QuestionnaireSerializer(questionnaire)

        return Response(serializer.data)


@api_view(['GET'])
def questionnaire_detail(request, pk):
    try:
        questionnaire = Questionnaire.objects.get(id=pk)
        serializer = QuestionnaireSerializer(questionnaire)
        return Response(serializer.data)
    except:
        raise Http404


class TestingView(APIView):
    def post(self, request):
        user = request.user
        result = request.data.get("answers")
        _id = request.data.get("questionnaireid")

        questionnaire = Questionnaire.objects.get(id=_id)
        print(questionnaire.title)
        true_answers = [item.id for item in questionnaire.questions.all()]
        print(true_answers)




        return Response({"success": "Request created successfully"})
