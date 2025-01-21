from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'content', 'featured_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'validate'}),
            'excerpt': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'content': CKEditor5Widget(
                attrs={'class': 'django_ckeditor_5'},
                config_name='default'
            )
        }