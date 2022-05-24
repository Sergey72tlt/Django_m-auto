from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django import forms


class LoginForm(AuthenticationForm):
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    username = UsernameField(label='', widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'}))
    error_messages = {'invalid_login': 'Введён неправильный логин или пароль'}