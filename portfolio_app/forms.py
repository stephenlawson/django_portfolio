from django.forms import ModelForm
from .models import Contact, ContactPhoto
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox


class ContactForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'captcha']

class PhotoForm(ModelForm):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea())
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
    class Meta:
        model = ContactPhoto
        fields = ['name', 'email', 'message', 'captcha']
