from django import forms
from django.forms import ModelForm
from .models import Inquiry
from products.models import Product
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class InquiryForm(forms.ModelForm):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)

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