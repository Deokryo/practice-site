from django import forms
from .models import  Post, Comment
from user.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude=('user', 'Post')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'nickname', 'email', 'intro')