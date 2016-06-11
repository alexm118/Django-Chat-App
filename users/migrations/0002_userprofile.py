# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 17:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(verbose_name='User Bio')),
                ('gravatar_username', models.CharField(max_length=50, verbose_name='Gravatr Username')),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.ChatUser')),
            ],
        ),
    ]
