from django.forms import ModelForm, TextInput
from .models import City, Facts

class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'City Name'})}

class FactForm(ModelForm):
    class Meta:
        model = Facts
        fields = '__all__'
        widgets = {'__all__': TextInput()}



