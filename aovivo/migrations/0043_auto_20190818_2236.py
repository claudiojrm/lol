# Generated by Django 2.2.4 on 2019-08-18 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0042_partida_jogadores_redside'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='jogadores_redside',
            field=models.ManyToManyField(to='jogador.Jogador'),
        ),
    ]
