from django import forms
from games_play_project.profile_app.models import ProfileModel


class CreateProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = ['email', 'age', 'password']

        widgets = {'password': forms.PasswordInput()}


class EditProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'profile_picture': 'Profile Picture'}
