# Generated by Django 2.0.1 on 2018-02-15 10:30

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('jeugdzorg', '0011_taggedregeling'),
    ]

    operations = [
        migrations.AddField(
            model_name='regeling',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='jeugdzorg.TaggedRegeling', to='jeugdzorg.RegelingTag', verbose_name='Tags'),
        ),
    ]