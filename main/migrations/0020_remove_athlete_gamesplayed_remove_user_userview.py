# Generated by Django 5.1.2 on 2024-11-18 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_athlete_sport'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='gamesPlayed',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userView',
        ),
    ]
