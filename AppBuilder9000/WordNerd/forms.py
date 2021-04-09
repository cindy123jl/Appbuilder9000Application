from django.forms import ModelForm
from .models import word, etymology
#ModelForm based of wordform mode
class wordform(ModelForm):
    class Meta:
        model = word
        fields = '__all__'
#ModelForm based of etymology model
class etymologyform(ModelForm):
    class Meta:
        model = etymology
        fields = '__all__'

