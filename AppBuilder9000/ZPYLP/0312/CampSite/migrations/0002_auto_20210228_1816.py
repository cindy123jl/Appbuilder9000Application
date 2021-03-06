# Generated by Django 2.2.5 on 2021-02-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CampSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campsite',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='campsite',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
