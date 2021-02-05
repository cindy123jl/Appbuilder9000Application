from django.forms import ModelForm
from .models import StrategyGame
from django import forms


class StrategyGamesForm(ModelForm):
    class Meta:
        model = StrategyGame
        fields = '__all__'
