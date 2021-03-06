# Generated by Django 2.2.5 on 2021-03-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AwesomeWeather', '0004_facts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facts',
            name='city',
        ),
        migrations.AddField(
            model_name='facts',
            name='town',
            field=models.CharField(blank=True, choices=[('Boaz', 'Boaz'), ('Portland', 'Portland'), ('Seattle', 'Seattle'), ('Miami', 'Miami'), ('Hilo', 'Hilo'), ('El Paso', 'El Paso')], max_length=200),
        ),
        migrations.AlterField(
            model_name='facts',
            name='date',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='facts',
            name='state',
            field=models.CharField(blank=True, choices=[('AL', 'AL'), ('OR', 'OR'), ('WA', 'WA'), ('FL', 'FL'), ('HI', 'HI'), ('TX', 'TX')], max_length=200),
        ),
    ]
