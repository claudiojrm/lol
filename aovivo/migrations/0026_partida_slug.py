# Generated by Django 2.2.4 on 2019-08-18 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0025_auto_20190818_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
