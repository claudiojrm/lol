# Generated by Django 2.2.4 on 2019-08-18 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campeonato', '0006_auto_20190818_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='campeonato',
            name='patch',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
