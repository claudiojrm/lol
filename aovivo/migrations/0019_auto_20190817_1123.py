# Generated by Django 2.2.4 on 2019-08-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0018_auto_20190816_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='kill_blueside',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partida',
            name='kill_redside',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
