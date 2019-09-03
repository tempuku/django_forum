from django import forms
from .models import Forum, Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Post
        field = 'desc'
