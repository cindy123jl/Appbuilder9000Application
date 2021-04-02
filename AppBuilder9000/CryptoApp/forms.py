from django.forms import ModelForm, DateField, DateInput
from .models import Currency, CoinStatus


class DateInput(DateInput):
    input_type = 'date'


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = ['chain_name', 'coin_unit', 'chain_type', 'launch_date']
        widgets = {'launch_date': DateInput()}


class CoinStatusForm(ModelForm):
    class Meta:
        model = CoinStatus
        fields = ['currency', 'value', 'as_of_date', 'supply', 'market_cap', 'transactions_per_sec']
        widgets = {'as_of_date': DateInput()}
