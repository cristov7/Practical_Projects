from django import forms
from .models import *


class BasePlantModelForm(forms.ModelForm):
    class Meta:
        model = PlantModel
        fields = '__all__'

        labels = {'plant_type': 'Type',
                  'name': 'Name',
                  'image_url': 'Image URL',
                  'description': 'Description',
                  'price': 'Price'}

        widgets = {'name': forms.TextInput(),
                   'image_url': forms.URLInput(),
                   'description': forms.Textarea(),
                   'price': forms.NumberInput(),
                   'profile': forms.HiddenInput()}


class CreatePlantModelModelForm(BasePlantModelForm):
    pass


class EditPlantModelModelForm(BasePlantModelForm):
    pass


class DeletePlantModelModelForm(BasePlantModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
