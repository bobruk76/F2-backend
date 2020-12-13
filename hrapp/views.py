import uuid

from rest_framework.utils import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf.global_settings import SECRET_KEY
from django.contrib.auth.models import User
from django.http import JsonResponse, Http404
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Question, Questionnaire, Result, Testing
from .serializers import QuestionSerializer, QuestionnaireSerializer, QuestionnaireListSerializer, ResultSerializer, \
    TestingSerializer
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
    @staticmethod
    def get_user(request):
        jwt_object = JWTAuthentication()
        header = jwt_object.get_header(request)
        raw_token = jwt_object.get_raw_token(header)
        validated_token = jwt_object.get_validated_token(raw_token)
        user = jwt_object.get_user(validated_token)
        return user

    def post(self, request):
        user = self.get_user(request)

        result = dict()
        result['questionnaire_id'] = uuid.UUID(request.data.get("questionnaireid"))

        answers = [uuid.UUID(item) for item in json.loads(request.data.get("answers"))]

        result['count_answers'] = len(answers)

        questionnaire = Questionnaire.objects.get(id=result['questionnaire_id'])
        questions_ids = [item.id for item in questionnaire.questions.all()]

        true_answers = set()
        result['count_questionnaire_answers'] = 0
        result['count_questionnaire_true_answers'] = 0

        for _id in questions_ids:
            question = Question.objects.get(id=_id)
            for answer in question.answers:
                result['count_questionnaire_answers'] += 1
                if answer.isTrue:
                    result['count_questionnaire_true_answers'] += 1
                    true_answers.add(answer.id)

        result['count_correct_answers'] = len(set(answers) & true_answers)
        result['count_incorrect_answers'] = result['count_answers'] - result['count_correct_answers']
        # testing = Testing.objects.get_or_create(username=user)
        # testing.results.add(result)
        # testing.save()

        Testing.objects.mongo_update({"username": user.username},
                                     {"$pull": {"results": {"questionnaire_id": result["questionnaire_id"]}}},
                                     True)

        Testing.objects.mongo_update({"username": user.username},
                                     {"$addToSet": {"results": result}},
                                     True)
        # serializer = TestingSerializer(testing)
        # return Response(serializer.data)

        return Response(result)

    @staticmethod
    def get_object(username):
        try:
            return Testing.objects.get(username=username)
        except:
            raise Http404

    def get(self, request, format=None):
        user = self.get_user(request)
        testing = self.get_object(user.username)
        serializer = TestingSerializer(testing)

        return Response(serializer.data)
