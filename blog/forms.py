from django import forms
from django.core.exceptions import ValidationError
from .models import Blog, Category


choices = [
    ('Events', 'Events'),
    ('Nya Tavlor', 'Nya Tavlor'),
    ('Blog', 'Blog'),
]

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'blog_url': forms.URLInput(attrs={'class': 'form-control',
                                       'placeholer': 'Lägg till länk till extern webbplats'})
        }