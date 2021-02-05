# from django import forms
#
from django.forms import ModelForm
from .models import Planet, Star, Galaxy


class PlanetForm(ModelForm):
    class Meta:
        model = Planet
        fields = '__all__'


class StarForm(ModelForm):
    class Meta:
        model = Star
        fields = '__all__'


class GalaxyForm(ModelForm):
    class Meta:
        model = Galaxy
        fields = '__all__'
