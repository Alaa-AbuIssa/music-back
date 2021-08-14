# Generated by Django 3.2.6 on 2021-08-13 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsApp', '0023_alter_song_song_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_type',
            field=models.CharField(choices=[('1', 'romantic'), ('2', 'rock'), ('3', 'soul'), ('4', 'classical'), ('5', 'folk '), ('6', 'hip hop ')], default='1', max_length=20),
        ),
    ]
