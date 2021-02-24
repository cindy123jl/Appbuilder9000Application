# Generated by Django 2.2.5 on 2021-02-24 20:26

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('state', models.CharField(choices=[('CA', 'California'), ('OR', 'Oregon'), ('WA', 'Washington')], max_length=2)),
                ('type', models.CharField(choices=[('Dispersed', 'Dispersed'), ('Developed', 'Developed')], max_length=9)),
                ('access', models.CharField(choices=[('Drive-up', 'Drive-up'), ('Hike-in', 'Hike-in')], max_length=8)),
                ('description', models.CharField(max_length=500)),
                ('fee', models.DecimalField(decimal_places=2, max_digits=5)),
                ('directions', models.CharField(blank=True, max_length=500, null=True)),
            ],
            managers=[
                ('Campsites', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('CA', 'California'), ('OR', 'Oregon'), ('WA', 'Washington')], max_length=2)),
                ('type', models.CharField(choices=[('Dispersed', 'Dispersed'), ('Developed', 'Developed')], max_length=9)),
                ('access', models.CharField(choices=[('Drive-up', 'Drive-up'), ('Hike-in', 'Hike-in')], max_length=8)),
                ('rating', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=2)),
                ('notes', models.CharField(blank=True, max_length=250, null=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CampSite.Campsite')),
            ],
            managers=[
                ('MySites', django.db.models.manager.Manager()),
            ],
        ),
    ]
