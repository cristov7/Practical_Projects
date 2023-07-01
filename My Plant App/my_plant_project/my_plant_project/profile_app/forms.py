from django import forms
from .models import *


class CreateProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ['profile_picture']

        labels = {'username': 'Username',
                  'first_name': 'First Name',
                  'last_name': 'Last Name'}


class EditProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        labels = {'username': 'Username',
                  'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'profile_picture': 'Profile Picture'}
