# Generated by Django 2.2.4 on 2019-08-18 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0027_remove_partida_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
