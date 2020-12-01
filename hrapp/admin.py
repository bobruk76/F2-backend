from django.contrib import admin
from .models import Question

# # Register your models here.
admin.site.register([Question])
#
# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('content',)
#     fields = ['id', 'content', 'answers', ]
