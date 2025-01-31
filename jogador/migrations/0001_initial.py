# Generated by Django 2.2.4 on 2019-08-16 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('apelido', models.CharField(max_length=200)),
                ('imagem', models.ImageField(upload_to='')),
                ('nacionalidade', models.CharField(max_length=100)),
                ('posicao', models.CharField(choices=[('adc', 'AD Carry'), ('jungle', 'Jungle'), ('mid', 'Mid Laner'), ('suporte', 'Suporte'), ('top', 'Top laner')], max_length=10)),
            ],
        ),
    ]
