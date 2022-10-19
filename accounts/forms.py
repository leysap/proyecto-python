from dataclasses import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MiFormularioDeCreacion(UserCreationForm):

    username = forms.CharField(label= 'Usuario', max_length = 20)
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña', widget=forms.PasswordInput)


    class meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { key: '' for key in fields}