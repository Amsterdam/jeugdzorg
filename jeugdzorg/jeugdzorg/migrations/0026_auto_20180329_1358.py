# Generated by Django 2.0.2 on 2018-03-29 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0025_organisatie_email_domeinen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='achternaam',
            field=models.CharField(blank=True, max_length=150, verbose_name='achternaam'),
        ),
        migrations.AddField(
            model_name='user',
            name='tussenvoegsel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tussenvoegsel'),
        ),
        migrations.AddField(
            model_name='user',
            name='voornaam',
            field=models.CharField(blank=True, max_length=100, verbose_name='voornaam'),
        ),
        migrations.AlterField(
            model_name='profiel',
            name='achternaam',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Achternaam'),
        ),
    ]