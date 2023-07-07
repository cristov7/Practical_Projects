from django import forms
from .models import ProfileModel


class CreateProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'image_url': 'Image URL'}

        widgets = {'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
                   'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
                   'image_url': forms.URLInput(attrs={'placeholder': 'URL'})}


class EditProfileModelModelForm(CreateProfileModelModelForm):
    pass


class DeleteProfileModelModelForm(CreateProfileModelModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
