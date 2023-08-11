from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from website.models import Subscriber


class SubscriberForms(ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=32)
