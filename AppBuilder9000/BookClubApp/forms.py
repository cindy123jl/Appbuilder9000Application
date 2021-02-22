from django.forms import ModelForm
from .models import Book
from django import forms


class BookForm(forms.ModelForm):
    # set read to true and hide on form
    read = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    # comments is not required on form
    comments = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Book
        fields = '__all__'
