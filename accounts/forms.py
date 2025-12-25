from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import DateInput

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}),
        required=True
    )

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'birth_date',
            'password1',
            'password2'
        ]
