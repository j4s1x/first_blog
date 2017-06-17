# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 04:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20170606_2033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('posts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.Posts')),
            ],
        ),
    ]