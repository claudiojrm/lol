# Generated by Django 2.2.4 on 2019-08-16 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0011_auto_20190816_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='blueside',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blueside', to='times.Times'),
        ),
    ]
