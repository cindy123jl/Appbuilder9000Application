from django.forms import ModelForm
from .models import Currency, CoinStatus


class CurrencyForm(ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'


class CoinStatusForm(ModelForm):
    class Meta:
        model = CoinStatus
        fields = '__all__'
