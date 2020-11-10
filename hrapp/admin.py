
from django.contrib import admin
from hrapp.models import Question, Answer, AnswerQuestion
# Register your models here.



@admin.register(Question)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Answer)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(AnswerQuestion)
class PostAdmin(admin.ModelAdmin):
    pass