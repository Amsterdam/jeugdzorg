# Generated by Django 2.0.1 on 2018-03-02 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0044_auto_20180302_1256'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactnaarthema',
            old_name='doel',
            new_name='thema',
        ),
        migrations.AlterUniqueTogether(
            name='contactnaarthema',
            unique_together={('contact', 'thema')},
        ),
    ]