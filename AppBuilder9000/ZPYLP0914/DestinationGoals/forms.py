from django.forms import ModelForm
from .models import Destination

class DestinationForm(ModelForm):
    class Meta:
        model = Destination
        fields = '__all__'



