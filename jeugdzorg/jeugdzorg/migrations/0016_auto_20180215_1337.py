# Generated by Django 2.0.1 on 2018-02-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0015_auto_20180215_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doel',
            options={'ordering': ['order'], 'verbose_name': 'Doel', 'verbose_name_plural': 'Doelen'},
        ),
        migrations.AddField(
            model_name='regeling',
            name='bron_url',
            field=models.URLField(blank=True, null=True, verbose_name='Bron url'),
        ),
    ]