# Generated by Django 2.2.5 on 2021-03-29 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CryptoApp', '0002_auto_20210325_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinstatus',
            name='currency',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='CryptoApp.Currency'),
        ),
    ]
