# Generated by Django 3.2.6 on 2021-08-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicsApp', '0009_auto_20210812_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
