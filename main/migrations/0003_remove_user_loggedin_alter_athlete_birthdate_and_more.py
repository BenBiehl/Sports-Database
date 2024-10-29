# Generated by Django 5.1.2 on 2024-10-28 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_user_loggedin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='loggedIn',
        ),
        migrations.AlterField(
            model_name='athlete',
            name='birthDate',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='height',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='weight',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]