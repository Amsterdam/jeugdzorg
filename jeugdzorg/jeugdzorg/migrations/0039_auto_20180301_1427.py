# Generated by Django 2.0.1 on 2018-03-01 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0038_auto_20180301_1417'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doel',
            options={'ordering': ['order'], 'verbose_name': 'Thema', 'verbose_name_plural': "Thema's"},
        ),
        migrations.AddField(
            model_name='doel',
            name='slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Url onderdeel'),
        ),
    ]
