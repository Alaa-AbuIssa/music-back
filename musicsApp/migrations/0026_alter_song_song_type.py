# Generated by Django 3.2.6 on 2021-08-14 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsApp', '0025_alter_song_song_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song_type',
            field=models.CharField(choices=[('romantic', '1-romantic'), ('rock', '2-rock'), ('soul', '3-soul'), ('classical', '4-classical'), ('folk', '5-folk'), ('hip hop', '6-hip hop')], default='1', max_length=20),
        ),
    ]