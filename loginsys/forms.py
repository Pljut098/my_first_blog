from django.forms.extras import SelectDateWidget
from django.http import JsonResponse
from django.views.generic.edit import CreateView

from .models import MyUser
from django import forms
from django.utils.translation import ugettext as _



class UserForm(forms.ModelForm):
    password = forms.CharField(label=_('Password'), required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


    username = forms.CharField(label=_('User Name'), required=True,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label=_('Email'), required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(widget=SelectDateWidget(
                             empty_label=("Choose Year", "Choose Month", "Choose Day")))

    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password','phone', 'avatar', 'date_of_birth']




class LoginForm(forms.Form):
    email = forms.EmailField(label=_('Email'), required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label=_('Password'), required=True,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))

