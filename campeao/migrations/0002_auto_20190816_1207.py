# Generated by Django 2.2.4 on 2019-08-16 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campeao', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campeao',
            options={'ordering': ['nome']},
        ),
    ]
