# Generated by Django 2.2.4 on 2019-08-17 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aovivo', '0021_auto_20190817_2326'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lance',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='lance',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
