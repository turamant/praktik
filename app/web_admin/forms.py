from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

from web_admin.models import New


User = get_user_model()

class NewCreateForm(forms.ModelForm):
    class Meta:
        model = New
        fields = '__all__'

class CustomUserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {'username': UsernameField}