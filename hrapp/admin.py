# from djongo import admin
from django.contrib import admin
from .models import Question

admin.site.register([Question])

# # Register your models here.
#
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('content',)
#     fields = ['content', 'answers', ]
