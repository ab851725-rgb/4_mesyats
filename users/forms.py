from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from captcha.fields import CaptchaField
from .models import CustomUser

class CustomRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'age',
            'city',
            'gender',
        )

class CustomLoginForm(AuthenticationForm):
    captcha = CaptchaField()