# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-22 04:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20170618_0349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='posts',
            new_name='post',
        ),
    ]
