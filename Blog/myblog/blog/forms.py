from django import forms
from .models import Post,Profile


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']   


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'country', 'mobile_no']