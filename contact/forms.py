from django import forms
from .models import Contact
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox


class ContactForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = Contact
        fields = ('name', 'email', 'topic', 'message', 'captcha',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'aria-label': 'Name',
                                           'placeholder': 'För- och efternamn *'}),
            'email': forms.EmailInput(attrs={'class': 'form-control',
                                             'aria-label': 'E-Mail',
                                             'placeholder': 'E-Mail *'}),
            'topic': forms.TextInput(attrs={'class': 'form-control',
                                            'aria-label': 'topic',
                                            'placeholder': 'Rubrik *'}),
            'message': forms.Textarea(attrs={'class': 'form-control',
                                             'aria-label': 'Message',
                                             'rows': 8,
                                             'placeholder': 'Meddelande'}),
            'captcha': ReCaptchaField(widget=ReCaptchaV2Checkbox()),
        }

    def __init__(self, *args, **kwargs):
        """
        Set autofocus on name field and remove auto-labels
        """
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            self.fields[field].label = False