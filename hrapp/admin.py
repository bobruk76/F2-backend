
from django.contrib import admin
from hrapp.models import Question
# Register your models here.


@admin.register(Question)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('content',)


