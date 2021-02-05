from django.forms import ModelForm
from .models import Cocktail

class CocktailForm(ModelForm):
    class Meta:
        model = Cocktail
        fields = '__all__'