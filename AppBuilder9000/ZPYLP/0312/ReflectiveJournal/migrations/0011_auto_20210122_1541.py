# Generated by Django 2.2.5 on 2021-01-22 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReflectiveJournal', '0010_auto_20210122_1537'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Activities',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Hours_Slept',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='Mood',
        ),
    ]
