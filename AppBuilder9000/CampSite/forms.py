from django import forms
from django.forms import ModelForm
from .models import Campsite, MySite


class CampsiteForm(ModelForm):
    class Meta:
        model = Campsite
        fields = '__all__'
        widgets = {
            'description': forms.Textarea,
            'amenities': forms.CheckboxSelectMultiple,
            'directions': forms.Textarea
        }


class MySiteForm(ModelForm):
    class Meta:
        model = MySite
        fields = '__all__'
