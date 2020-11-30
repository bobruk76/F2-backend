from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['content', 'isTrue', ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = ['content', 'answers', ]
#
# {
#     "content": "Первый вопрос",
#     "answers": [{"content": "Первый ответ", "isTrue": "True"},{"content": "Второй ответ", "isTrue": "False"}]
# }
