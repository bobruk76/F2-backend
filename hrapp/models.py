import uuid

from djongo import models
from django import forms
from django.contrib.auth.models import User
# Create your models here.


class Answer(models.Model):
    id = models.UUIDField(default=uuid.uuid4)
    content = models.CharField(max_length=255, verbose_name="Текст ответа")
    isTrue = models.BooleanField(default=False, verbose_name="Правильный ответ")

    class Meta:
        abstract = True
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'

    def __str__(self):
        return f'{self.content}'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('id', 'content', 'isTrue')


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=255, verbose_name="Текст вопроса")
    answers = models.ArrayField(
        model_container=Answer,
        model_form_class=AnswerForm,
    )

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.content}'

    objects = models.DjongoManager()
