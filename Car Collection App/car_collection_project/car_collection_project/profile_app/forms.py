from django import forms
from .models import *


class CreateProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['first_name', 'last_name', 'profile_picture']

        labels = {'username': 'Username',
                  'email': 'Email',
                  'age': 'Age',
                  'password': 'Password'}

        widgets = {'password': forms.PasswordInput()}


class EditProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        labels = {'username': 'Username',
                  'email': 'Email',
                  'age': 'Age',
                  'password': 'Password',
                  'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'profile_picture': 'Profile Picture'}
