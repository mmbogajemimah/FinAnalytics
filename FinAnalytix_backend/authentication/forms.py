from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import Group, User
from django.contrib.auth import get_user_model

# User = get_user_model()

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=200, required=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')