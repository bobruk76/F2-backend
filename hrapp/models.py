import uuid

from djongo import models
from tinymce import models as tinymce_models
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
        return f'{self.id}'


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('id', 'content', 'isTrue')


class Question(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default='', verbose_name="Заголовок вопроса")
    content = tinymce_models.HTMLField(default='', verbose_name="Текст вопроса")
    answers = models.ArrayField(
        model_container=Answer,
        model_form_class=AnswerForm,
    )

    class Meta:
        verbose_name = 'Вопросы'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.title}'

    objects = models.DjongoManager()


class Questionnaire(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255,  default='', verbose_name="Название опросника")

    questions = models.ArrayReferenceField(
        to=Question,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = 'Опросник'
        verbose_name_plural = 'Опросник'

    def __str__(self):
        return f'{self.title}'

    objects = models.DjongoManager()


class Result(models.Model):
    questionnaire_id = models.UUIDField()
    count_questionnaire_answers = models.IntegerField(default=0)
    count_questionnaire_true_answers = models.IntegerField(default=0)

    count_correct_answers = models.IntegerField(default=0)
    count_answers = models.IntegerField(default=0)

    class Meta:
        abstract = True


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'


class Testing(models.Model):
    username = models.CharField(max_length=255, primary_key=True, editable=False)
    results = models.ArrayField(
        model_container=Result,
        model_form_class=ResultForm,
    )

    class Meta:
        verbose_name = 'Итоги тестирования'
        verbose_name_plural = 'Итоги тестирования'

    objects = models.DjongoManager()
