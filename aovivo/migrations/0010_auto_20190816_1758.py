# Generated by Django 2.2.4 on 2019-08-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0009_partida_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lance',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pré jogo'), (2, 'Pick e Bans'), (3, 'Em andamento'), (4, 'Jogo Pausado'), (5, 'Pós Jogo'), (6, 'Encerrado')], default=1),
        ),
    ]
