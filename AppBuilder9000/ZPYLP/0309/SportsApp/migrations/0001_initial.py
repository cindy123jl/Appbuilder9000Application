# Generated by Django 2.2.5 on 2021-01-14 21:09

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SavedNbaGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('home_team', models.CharField(choices=[('Atlanta Hawks', 'Atlanta Hawks'), ('Boston Celtics', 'Boston Celtics'), ('Brooklyn Nets', 'Brooklyn Nets'), ('Charlotte Hornets', 'Charlotte Hornets'), ('Chicago Bulls', 'Chicago Bulls'), ('Cleveland Cavaliers', 'Cleveland Cavaliers'), ('Dallas Mavericks', 'Dallas Mavericks'), ('Denver Nuggets', 'Denver Nuggets'), ('Detroit Pistons', 'Detroit Pistons'), ('Golden State Warriors', 'Golden State Warriors'), ('Houston Rockets', 'Houston Rockets'), ('Indiana Pacers', 'Indiana Pacers'), ('Los Angeles Clippers', 'Los Angeles Clippers'), ('Los Angeles Lakers', 'Los Angeles Lakers'), ('Memphis Grizzlies', 'Memphis Grizzlies'), ('Miami Heat', 'Miami Heat'), ('Milwaukee Bucks', 'Milwaukee Bucks'), ('Minnesota Timberwolves', 'Minnesota Timberworves'), ('New Orleans Pelicans', 'New Orleans Pelicans'), ('New York Knicks', 'New York Knicks'), ('Oklahoma City Thunder', 'Oklahoma City Thunder'), ('Orlando Magic', 'Orlando Magic'), ('Philadelphia 76ers', 'Philadelphia 76ers'), ('Phoenix Suns', 'Phoenix Suns'), ('Portland Trailblazers', 'Portland Trailblazers'), ('Sacramento Kings', 'Sacramento Kings'), ('San Antonio Spurs', 'San Antonio Spurs'), ('Toronto Raptors', 'Toronto Raptos'), ('Utah Jazz', 'Utah Jazz'), ('Washington Wizards', 'Washington Wizards')], max_length=50)),
                ('away_team', models.CharField(choices=[('Atlanta Hawks', 'Atlanta Hawks'), ('Boston Celtics', 'Boston Celtics'), ('Brooklyn Nets', 'Brooklyn Nets'), ('Charlotte Hornets', 'Charlotte Hornets'), ('Chicago Bulls', 'Chicago Bulls'), ('Cleveland Cavaliers', 'Cleveland Cavaliers'), ('Dallas Mavericks', 'Dallas Mavericks'), ('Denver Nuggets', 'Denver Nuggets'), ('Detroit Pistons', 'Detroit Pistons'), ('Golden State Warriors', 'Golden State Warriors'), ('Houston Rockets', 'Houston Rockets'), ('Indiana Pacers', 'Indiana Pacers'), ('Los Angeles Clippers', 'Los Angeles Clippers'), ('Los Angeles Lakers', 'Los Angeles Lakers'), ('Memphis Grizzlies', 'Memphis Grizzlies'), ('Miami Heat', 'Miami Heat'), ('Milwaukee Bucks', 'Milwaukee Bucks'), ('Minnesota Timberwolves', 'Minnesota Timberworves'), ('New Orleans Pelicans', 'New Orleans Pelicans'), ('New York Knicks', 'New York Knicks'), ('Oklahoma City Thunder', 'Oklahoma City Thunder'), ('Orlando Magic', 'Orlando Magic'), ('Philadelphia 76ers', 'Philadelphia 76ers'), ('Phoenix Suns', 'Phoenix Suns'), ('Portland Trailblazers', 'Portland Trailblazers'), ('Sacramento Kings', 'Sacramento Kings'), ('San Antonio Spurs', 'San Antonio Spurs'), ('Toronto Raptors', 'Toronto Raptos'), ('Utah Jazz', 'Utah Jazz'), ('Washington Wizards', 'Washington Wizards')], max_length=50)),
                ('date_game', models.DateField()),
                ('time_start', models.TimeField()),
            ],
            managers=[
                ('SavedNbaGame', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='FavPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('favorite_player', models.CharField(max_length=50)),
                ('corresponding_team', models.ForeignKey(choices=[('Atlanta Hawks', 'Atlanta Hawks'), ('Boston Celtics', 'Boston Celtics'), ('Brooklyn Nets', 'Brooklyn Nets'), ('Charlotte Hornets', 'Charlotte Hornets'), ('Chicago Bulls', 'Chicago Bulls'), ('Cleveland Cavaliers', 'Cleveland Cavaliers'), ('Dallas Mavericks', 'Dallas Mavericks'), ('Denver Nuggets', 'Denver Nuggets'), ('Detroit Pistons', 'Detroit Pistons'), ('Golden State Warriors', 'Golden State Warriors'), ('Houston Rockets', 'Houston Rockets'), ('Indiana Pacers', 'Indiana Pacers'), ('Los Angeles Clippers', 'Los Angeles Clippers'), ('Los Angeles Lakers', 'Los Angeles Lakers'), ('Memphis Grizzlies', 'Memphis Grizzlies'), ('Miami Heat', 'Miami Heat'), ('Milwaukee Bucks', 'Milwaukee Bucks'), ('Minnesota Timberwolves', 'Minnesota Timberworves'), ('New Orleans Pelicans', 'New Orleans Pelicans'), ('New York Knicks', 'New York Knicks'), ('Oklahoma City Thunder', 'Oklahoma City Thunder'), ('Orlando Magic', 'Orlando Magic'), ('Philadelphia 76ers', 'Philadelphia 76ers'), ('Phoenix Suns', 'Phoenix Suns'), ('Portland Trailblazers', 'Portland Trailblazers'), ('Sacramento Kings', 'Sacramento Kings'), ('San Antonio Spurs', 'San Antonio Spurs'), ('Toronto Raptors', 'Toronto Raptos'), ('Utah Jazz', 'Utah Jazz'), ('Washington Wizards', 'Washington Wizards')], on_delete=django.db.models.deletion.CASCADE, to='SportsApp.SavedNbaGame')),
            ],
            managers=[
                ('FavPlayer', django.db.models.manager.Manager()),
            ],
        ),
    ]
