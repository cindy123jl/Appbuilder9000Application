# Generated by Django 2.2.5 on 2021-01-22 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AlbumTracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
