# Generated by Django 2.2.4 on 2019-08-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regiao', '0004_regiao_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regiao',
            name='slug',
            field=models.SlugField(editable=False),
        ),
    ]
