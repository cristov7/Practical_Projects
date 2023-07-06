from django import forms
from .models import GameModel


class CreateGameModelModelForm(forms.ModelForm):
    class Meta:
        model = GameModel
        fields = '__all__'

        labels = {'max_level': 'Max Level',
                  'image_url': 'Image URL'}

        widgets = {'summary': forms.Textarea(),
                   'profile': forms.HiddenInput()}


class EditGameModelModelForm(CreateGameModelModelForm):
    pass


class DeleteGameModelModelForm(CreateGameModelModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
