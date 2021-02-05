from django.forms import ModelForm
from django import forms
from .models import Book, Author


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {'date_published': forms.SelectDateWidget(years=range(2021, 1940, -1))}


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

