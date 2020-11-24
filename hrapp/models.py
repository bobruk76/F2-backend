from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Question(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    author = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопрос'

    def __str__(self):
        return f'{self.title}'


class Answer(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField
    question = models.ManyToManyField(Question, blank=True, related_name='answer', through='AnswerQuestion')

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'

    def __str__(self):
        return f'{self.title}'


class AnswerQuestion(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question')
    isTrue = models.BooleanField(default=False)

