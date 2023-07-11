from django import forms
from .models import *


class CreateProfileModelModelForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

        labels = {'first_name': 'First Name',
                  'last_name': 'Last Name',
                  'image_url': 'Link to Profile Image'}


class AddNoteModelModelForm(forms.ModelForm):
    class Meta:
        model = NoteModel
        fields = '__all__'

        labels = {'image_url': 'Link to Image'}

        widgets = {'content': forms.Textarea(),
                   'profile': forms.HiddenInput()}


class EditNoteModelModelForm(AddNoteModelModelForm):
    pass


class DeleteNoteModelModelForm(AddNoteModelModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
