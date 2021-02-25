from django import forms
from django.forms import ModelForm
from .models import Campsite


class CampsiteForm(ModelForm):
    class Meta:
        model = Campsite
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(),
            'directions': forms.Textarea(),
        }



