from django import forms
from .models import Answer, Question
from tinymce.widgets import TinyMCE


class QuestionAdminForm(forms.Form):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = Question
        fields = ('id', 'content', 'answers')

