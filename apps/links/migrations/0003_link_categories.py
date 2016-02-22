# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 14:25
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('links', '0002_link_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='categories',
            field=taggit.managers.TaggableManager(
                help_text='A comma-separated list of tags.',
                through='taggit.TaggedItem',
                to='taggit.Tag',
                verbose_name='Tags'
            ),
        ),
    ]
