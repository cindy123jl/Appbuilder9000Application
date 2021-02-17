# Generated by Django 2.2.5 on 2020-09-08 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NSW_App', '0002_auto_20200908_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='ESRB_rating',
            field=models.CharField(blank=True, choices=[('Everyone', 'Everyone'), ('Everyone 10+', 'Everyone 10+'), ('Teen', 'Teen'), ('Mature 17+', 'Mature 17+'), ('Adults Only 18+', 'Adults Only 18+'), ('Rating Pending', 'Rating Pending')], db_column='ESRB', max_length=20, null=True, verbose_name='ESRB Rating'),
        ),
    ]