# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 03:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='posts',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Posts'),
        ),
    ]
