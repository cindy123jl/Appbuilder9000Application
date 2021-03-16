from django import forms
from .models import Planner, zone_type
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



class PlannerForm(forms.ModelForm):
    zone = forms.ChoiceField(choices= zone_type)


    class Meta:
        model = Planner
        fields = '__all__'

    def __init__(self, *args, **kwargs):    # overide forms.ModelForm
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save_plan', 'Save Garden Plan'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-dnager'))


