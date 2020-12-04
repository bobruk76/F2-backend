from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['content', 'isTrue', ]


class QuestionSerializer(serializers.ModelSerializer):
    # answers = AnswerSerializer(many=True)
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
