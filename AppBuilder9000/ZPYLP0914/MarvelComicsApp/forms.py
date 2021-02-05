from django.forms import ModelForm, DateInput
from .models import Character, Favorite


class CreateCharacter(ModelForm):
    class Meta:
        #grabbing the model 'Subscriber' and putting it in the variable 'model'
        model = Character
        #display all fields from the 'Subscriber' model
        fields = '__all__'
        #use the default django widget 'DateInput' for the 'sub-dob' field in the 'Subscriber' model
        widgets = {
            'dob': DateInput(attrs={'type': 'date'})
        }

class SaveFavorite(ModelForm):
    class Meta:
        model = Favorite
        fields = '__all__'

