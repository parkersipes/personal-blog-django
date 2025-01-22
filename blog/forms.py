from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'topic', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-white',
                'placeholder': 'Enter post title'
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-white',
                'rows': '3',
                'placeholder': 'Write a brief excerpt'
            }),
            'topic': forms.Select(attrs={
                'class': 'form-select bg-dark text-white'
            }),
            'content': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'},
                config_name='default'
            ),
        }