# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-15 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='messages',
            name='message',
            field=models.TextField(null=True),
        ),
    ]
