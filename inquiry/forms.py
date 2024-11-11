from django import forms
from django.forms import ModelForm
from .models import Inquiry
from products.models import Product


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on first name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False