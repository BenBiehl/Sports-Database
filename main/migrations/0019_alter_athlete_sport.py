# Generated by Django 5.1.2 on 2024-11-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_athlete_numviews_alter_baseballstat_homeruns_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='sport',
            field=models.CharField(choices=[('baseball', 'baseball'), ('basketball', 'basketball'), ('soccer', 'soccer'), ('football', 'football')], default='Baseball', max_length=20),
        ),
    ]
