# Generated by Django 2.2.5 on 2020-10-04 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigfootApp', '0003_auto_20201003_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='country',
            field=models.CharField(choices=[('Canada', 'Canada'), ('United States', 'United States')], max_length=60),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='state',
            field=models.CharField(choices=[('Alberta', 'AB'), ('Alaska', 'AK'), ('Alabama', 'AL'), ('Arkansas', 'AR'), ('Arizona', 'AZ'), ('British Columbia', 'BC'), ('California', 'CA'), ('Colorado', 'CO'), ('Connecticut', 'CT'), ('Washington DC', 'DC'), ('Delaware', 'DE'), ('Florida', 'FL'), ('Georgia', 'GA'), ('Hawaii', 'HI'), ('Iowa', 'IA'), ('Idaho', 'ID'), ('Illinois', 'IL'), ('Indiana', 'IN'), ('Kansas', 'KS'), ('Kentucky', 'KY'), ('Louisiana', 'LA'), ('Massachusetts', 'MA'), ('Manitoba', 'MB'), ('Maryland', 'MD'), ('Maine', 'ME'), ('Michigan', 'MI'), ('Minnesota', 'MN'), ('Missouri', 'MO'), ('Mississippi', 'MS'), ('Montana', 'MT'), ('New Brunswick', 'NB'), ('North Carolina', 'NC'), ('North Dakota', 'ND'), ('Nebraska', 'NE'), ('New Hampshire', 'NH'), ('New Jersey', 'NJ'), ('Newfoundland', 'NL'), ('New Mexico', 'NM'), ('Nova Scotia', 'NS'), ('Northwest Territories', 'NT'), ('Nunavut', 'NU'), ('Nevada', 'NV'), ('New York', 'NY'), ('Ohio', 'OH'), ('Oklahoma', 'OK'), ('Ontario', 'ON'), ('Oregon', 'OR'), ('Pennsylvania', 'PA'), ('Prince Edward Island', 'PE'), ('Quebec', 'QC'), ('Rhode Island', 'RI'), ('South Carolina', 'SC'), ('South Dakota', 'SD'), ('Saskatchewan', 'SK'), ('Tennessee', 'TN'), ('Texas', 'TX'), ('Utah', 'UT'), ('Vermont', 'VT'), ('Washington', 'WA'), ('Wisconsin', 'WI'), ('West Virgina', 'WV'), ('Wyoming', 'WY'), ('Yukon', 'YT')], max_length=80, verbose_name='State or Province'),
        ),
    ]