# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-28 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0009_add_items_to_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='first_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='last_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='zipcode',
            field=models.PositiveIntegerField(default=90401),
        ),
    ]