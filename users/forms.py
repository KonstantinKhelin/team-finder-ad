from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["name", "surname", "email", "github_url", "phone", "avatar", "about",]

class CustomAuthenticationForm(AuthenticationForm):
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'autofocus': True})
    )
    password = forms.CharField(
        label='Пароль',
        strip=False,
        widget=forms.PasswordInput()
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)  # Сохраняем request
        super().__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(
                email=email,
                password=password
            )
            if self.user_cache is None:
                if self.user_cache is None:
                    raise forms.ValidationError(
                'Пользователь с таким email не найден.',
                code='no_user'
            )
                elif not self.user_cache.is_active:
                    raise forms.ValidationError(
                'Аккаунт деактивирован.',
                code='inactive'
            )
                else:
                    raise forms.ValidationError(
                'Неверные email или пароль.',
                code='invalid_login'
            )
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
