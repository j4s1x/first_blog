from django import forms
from .models import Posts, Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','text']
        labels = {'name':'name:','text': 'comment:'}
