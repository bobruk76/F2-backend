import uuid

from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.fields import SerializerMethodField

from .models import Question, Answer, Testing, Questionnaire, Result


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'answers', ]
    
    def get_answers(self, obj):
        return_data = None
        if type(obj.answers) == list:
            embedded_list = []
            for item in obj.answers:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.answers.__dict__
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        return return_data


class QuestionnaireListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = ['id', 'title', ]


class QuestionnaireSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Questionnaire
        fields = ['id', 'title', 'questions', ]


class ResultSerializer(serializers.ModelSerializer):

    class Meta:
        model = Result
        fields = '__all__'


class TestingSerializer(serializers.ModelSerializer):
    results = serializers.SerializerMethodField()

    class Meta:
        model = Testing
        fields = ['username', 'results', ]

    def get_results(self, obj):
        return_data = None
        if type(obj.results) == list:
            embedded_list = []
            for item in obj.results:
                embedded_dict = item.__dict__
                for key in list(embedded_dict.keys()):
                    if key.startswith('_'):
                        embedded_dict.pop(key)
                embedded_list.append(embedded_dict)
            return_data = embedded_list
        else:
            embedded_dict = obj.results.__dict__
            for key in list(embedded_dict.keys()):
                if key.startswith('_'):
                    embedded_dict.pop(key)
            return_data = embedded_dict
        for item in return_data:
            item['title'] = Questionnaire.objects.get(id=item['questionnaire_id']).title

        return return_data
