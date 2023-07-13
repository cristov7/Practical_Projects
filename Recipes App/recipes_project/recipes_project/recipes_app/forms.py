from django import forms
from .models import *


class CreateRecipeModelModelForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = '__all__'

        labels = {'image_url': 'Image URL',
                  'time': 'Time (Minutes)'}

        widgets = {'description': forms.Textarea()}


class EditRecipeModelModelForm(CreateRecipeModelModelForm):
    pass


class DeleteRecipeModelModelForm(CreateRecipeModelModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
