from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class MiFormularioDeCreacion(UserCreationForm):

    username = forms.CharField(label='Usuario', max_length=20)
    email = forms.CharField()
    password1 = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repetir Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = { key: '' for key in fields}

class EdidarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')