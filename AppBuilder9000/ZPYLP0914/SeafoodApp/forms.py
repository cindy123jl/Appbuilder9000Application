from django.forms import ModelForm
from .models import Seafood
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class SeafoodForm(ModelForm):
    class Meta:
        model = Seafood
        fields = '__all__'
        widgets = {
            'harvested_during': DateInput()
        }
