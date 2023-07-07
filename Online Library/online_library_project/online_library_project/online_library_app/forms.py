from django import forms
from .models import BookModel


class AddBookModelModelForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = '__all__'

        labels = {'type_book': 'Type'}

        widgets = {'title': forms.TextInput(attrs={'placeholder': 'Title'}),
                   'description': forms.Textarea(attrs={'placeholder': 'Description'}),
                   'image': forms.URLInput(attrs={'placeholder': 'Image'}),
                   'type_book': forms.TextInput(attrs={'placeholder': 'Fiction, Novel, Crime...'}),
                   'profile': forms.HiddenInput()}


class EditBookModelModelForm(AddBookModelModelForm):
    pass
