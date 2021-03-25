from django.db import models


chain_types = [
    ('Proof of Work', 'Proof of Work'),
    ('Proof of Stake', 'Proof of Stake'),
    ('Other', 'Other')
]


class Currency(models.Model):
    chain_name = models.CharField(max_length=60)
    coin_unit = models.CharField(max_length=60)
    chain_type = models.CharField(max_length=200, choices=chain_types)
    # Will need some kind of guidance and controls on date entry fields
    launch_year = models.IntegerField(default=0)

    Currencies = models.Manager()

    def __str__(self):
        return self.chain_name


class CoinStatus(models.Model):
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=20, decimal_places=6)
    as_of_date = models.DateField(auto_now=False, auto_now_add=False)
    supply = models.DecimalField(max_digits=20, decimal_places=2)
    market_cap = models.DecimalField(max_digits=20, decimal_places=2)
    transactions_per_sec = models.DecimalField(max_digits=20, decimal_places=2)

    CoinStatuses = models.Manager()

    def __str__(self):
        return self.currency
