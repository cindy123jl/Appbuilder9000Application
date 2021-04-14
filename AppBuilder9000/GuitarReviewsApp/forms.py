from django import forms
from .models import GuitarInfo

# creates form
class GuitarForm(forms.ModelForm):
    # choosing the model we can to use
    class Meta:
        model = GuitarInfo
        fields = "__all__"
