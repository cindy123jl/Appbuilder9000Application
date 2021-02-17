# Generated by Django 2.2.5 on 2020-12-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DestinationGoals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='destination',
            name='image',
        ),
        migrations.AlterField(
            model_name='destination',
            name='type',
            field=models.CharField(choices=[('City', 'City'), ('Country', 'Country'), ('State', 'State')], max_length=60),
        ),
    ]