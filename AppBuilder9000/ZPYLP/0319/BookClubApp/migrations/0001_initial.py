# Generated by Django 2.2.5 on 2021-02-19 00:23

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('image', models.URLField()),
                ('read', models.BooleanField()),
            ],
            managers=[
                ('Books', django.db.models.manager.Manager()),
            ],
        ),
    ]
