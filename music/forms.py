from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'artist', 'text',)

class DeleteNewForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'artist', 'text',]