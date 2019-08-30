from django import forms
from .models import Forum, Comment

class ForumForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = 'title'
