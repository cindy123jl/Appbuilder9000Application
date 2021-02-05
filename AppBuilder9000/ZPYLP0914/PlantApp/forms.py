from django.forms import ModelForm
from .models import Indoor_Plant


class Indoor_PlantForm(ModelForm):
    class Meta:
        model = Indoor_Plant
        fields = '__all__'
