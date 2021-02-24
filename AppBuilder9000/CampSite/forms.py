from django.forms import ModelForm
from .models import Campsite, MySite


class CampsiteForm(ModelForm):
    class Meta:
        model = Campsite
        fields = '__all__'


class MySiteForm(ModelForm):
    class Meta:
        model = MySite
        fields = '__all__'
