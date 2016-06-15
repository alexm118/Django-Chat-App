# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-12 01:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160611_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='gravatar_username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gravatar_email',
            field=models.EmailField(default='alexm118@vt.edu', max_length=254, verbose_name='Gravatr Email'),
            preserve_default=False,
        ),
    ]