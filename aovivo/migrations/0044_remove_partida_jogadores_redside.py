# Generated by Django 2.2.4 on 2019-08-18 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0043_auto_20190818_2236'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='jogadores_redside',
        ),
    ]
