from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Singupform(UserCreationForm):
    email = forms.EmailField(max_length=25, help_text='batnuoc')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )