# Generated by Django 2.2.4 on 2019-08-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0033_auto_20190818_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='lance',
            name='stats',
            field=models.CharField(blank=True, choices=[('barão', 'Barão de Nashor'), ('drag-anciao', 'Dragão ancião'), ('drag-infernal', 'Dragão infernal'), ('drag-montanha', 'Dragão da montanha'), ('drag-oceano', 'Dragão do oceano'), ('drag-vento', 'Dragão de vento')], max_length=20),
        ),
    ]
