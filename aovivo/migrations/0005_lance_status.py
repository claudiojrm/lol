# Generated by Django 2.2.4 on 2019-08-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0004_auto_20190816_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='lance',
            name='status',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
