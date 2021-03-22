from django import forms
from .models import Planner, zone_type, Eval
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column


class PlannerForm(forms.ModelForm):
    Growing_Year = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'current year i.e. 2021'}))
    Growing_Zone = forms.ChoiceField(choices=zone_type)
    Sowing_Time_Frame = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'months i.e. March-April or soil temp'}))
    Harvest_Tips = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'time, plant size, and how to harvest'}))
    General_Care_Tips = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'sunshine/shade, watering needs, nutrient needs, weeding protocol'}))

    class Meta:
        model = Planner
        fields = '__all__'

    def __init__(self, *args, **kwargs):  # overide forms.ModelForm
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', 'Save'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-dnager'))

        self.helper.layout = Layout(
            Column('Vegetable_Name'),
            Row(
                Column('Growing_Year'),
                Column('Growing_Zone')
            ),
            Column('Sowing_Time_Frame'),
            Column('Harvest_Tips'),
            Column('General_Care_Tips')
        )


class EvalForm(forms.ModelForm):
    Growing_Season_Observations = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'seasonal notes: when did seeds sprout? new cover crop? new companion planting method?'}))
    Harvest_Weight = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'weight in lbs'}))
    Harvest_Observations = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'harvest notes i.e. rainfall/weather events, pest control, successes/failures'}))

    def __init__(self, *args, **kwargs):  # overide forms.ModelForm
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('save', 'Save'))
        self.helper.add_input(Submit('cancel', 'Cancel', css_class='btn btn-dnager'))

        self.helper.layout = Layout(
            Column('Vegetable_Name'),
            Column('Growing_Season_Observations'),
            Column('Harvest_Weight'),
            Column('Harvest_Observations')
        )

    class Meta:
        model = Eval
        fields = '__all__'
