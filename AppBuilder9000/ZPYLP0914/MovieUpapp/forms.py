from django import forms
from django.forms import ModelForm
from .models import Movie

class DateInput(forms.DateInput):
    input_type = 'date'

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        widgets = {
            'release_date': DateInput(),
            }
