# Generated by Django 2.0.2 on 2018-03-09 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiel',
            name='vaardigheden',
            field=models.TextField(blank=True, null=True, verbose_name='Vaardigheden'),
        ),
    ]