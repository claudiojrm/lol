# Generated by Django 2.2.4 on 2019-08-18 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0024_auto_20190817_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lance',
            name='titulo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
