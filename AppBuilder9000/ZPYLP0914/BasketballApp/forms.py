from django.forms import ModelForm
from .models import CreatePlayer


class CreatePlayerForm(ModelForm):
    class Meta:
        model = CreatePlayer
        fields = '__all__'
