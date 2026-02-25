from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["name", "surname", "email", "github_url", "phone", "avatar", "about",]
