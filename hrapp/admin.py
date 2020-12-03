from django.contrib import admin
from .models import Question, Questionnaire
from .forms import QuestionAdminForm

# # Register your models here.
admin.site.register([Question, Questionnaire])


# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('content',)
#     fields = ['id', 'content', 'answers', ]
#     form = QuestionAdminForm
