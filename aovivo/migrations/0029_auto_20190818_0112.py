# Generated by Django 2.2.4 on 2019-08-18 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0028_partida_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
