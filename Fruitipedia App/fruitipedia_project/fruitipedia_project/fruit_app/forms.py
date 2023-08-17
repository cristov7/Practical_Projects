from django import forms
from .models import FruitModel


class CreateFruitModelModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        fields = '__all__'

        labels = {'name': '',
                  'image_url': '',
                  'description': '',
                  'nutrition': ''}

        widgets = {'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
                   'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
                   'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'}),
                   'profile': forms.HiddenInput()}


class EditFruitModelModelForm(CreateFruitModelModelForm):
    labels = {'name': 'Name',
              'image_url': 'Image URL',
              'description': 'Description',
              'nutrition': 'Nutrition'}


class DeleteFruitModelModelForm(forms.ModelForm):
    class Meta:
        model = FruitModel
        exclude = ['nutrition', 'profile']

        labels = {'name': 'Name',
                  'image_url': 'Image URL',
                  'description': 'Description'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
