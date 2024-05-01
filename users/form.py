from django.contrib.auth import get_user_model
from django import forms

UsersModel = get_user_model()

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UsersModel
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)