# Generated by Django 5.1.2 on 2024-11-13 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_athlete_age_alter_athlete_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseballstat',
            name='battingAvg',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='baseballstat',
            name='homeRuns',
            field=models.FloatField(blank=True),
        ),
    ]