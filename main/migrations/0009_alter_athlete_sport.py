# Generated by Django 5.1.2 on 2024-10-31 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_athlete_age_alter_athlete_joinyear_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='sport',
            field=models.CharField(choices=[('Baseball', 'Baseball'), ('Basketball', 'Basketball'), ('Soccer', 'Soccer'), ('Football', 'Football')], default='Baseball', max_length=20),
        ),
    ]
