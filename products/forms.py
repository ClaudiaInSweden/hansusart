from django import forms
from .widgets import CustomClearableFileInput
from crispy_forms import bootstrap, layout
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=True,
                             widget=CustomClearableFileInput),
    categories = forms.Select(attrs={'class': 'form-control', 
                             'aria-label': 'Category'}),

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_name = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['categories'].choices = friendly_name
