# Generated by Django 2.0.1 on 2018-03-01 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0036_remove_eventitem_naam'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventitem',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Naam'),
        ),
    ]
