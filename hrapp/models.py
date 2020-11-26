from djongo import models
from django.contrib.auth.models import User
# Create your models here.


class Answer(models.Model):
    content = models.CharField(max_length=255, blank=False, default='')
    isTrue = models.BooleanField(default=False)

    class Meta:
        abstract = True
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответ'

    def __str__(self):
        return self.content


class Question(models.Model):
    content = models.CharField(max_length=255, blank=False, default='')
    author = models.ForeignKey(User, null=True, default=None)
    answers = models.ArrayField(
        model_container=Answer,
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопрос'

    def __str__(self):
        return f'{self.content}'

