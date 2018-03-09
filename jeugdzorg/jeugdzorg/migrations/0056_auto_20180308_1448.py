# Generated by Django 2.0.2 on 2018-03-08 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0055_auto_20180308_1048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiel',
            options={'ordering': ('achternaam',), 'verbose_name': 'Profiel', 'verbose_name_plural': 'Profielen'},
        ),
        migrations.AddField(
            model_name='profiel',
            name='zichtbaar',
            field=models.BooleanField(default=True, help_text='Haal het vinkje, als je wil dat dit profiel onzichtbaar is voor andere.', verbose_name='Zichtbaar'),
        ),
    ]
