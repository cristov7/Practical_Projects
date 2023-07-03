from django import forms
from .models import *


class BaseCarModelModelForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'

        labels = {'car_type': 'Type',
                  'car_model': 'Model',
                  'year': 'Year',
                  'image_url': 'Image URL',
                  'price': 'Price'}

        widgets = {'profile': forms.HiddenInput()}


class CreateCarModelModelForm(BaseCarModelModelForm):
    pass


class EditCarModelModelForm(BaseCarModelModelForm):
    pass


class DeleteCarModelModelForm(BaseCarModelModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
