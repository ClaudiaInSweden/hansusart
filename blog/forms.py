from django import forms
from django.core.exceptions import ValidationError
from .models import Blog, Category


choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        widgets = {
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'})
        }