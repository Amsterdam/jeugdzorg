# Generated by Django 2.0.1 on 2018-02-22 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0022_regeling_bron_html_query'),
    ]

    operations = [
        migrations.AddField(
            model_name='regeling',
            name='bron_veranderd',
            field=models.BooleanField(default=False, verbose_name='Bron veranderd'),
        ),
    ]
