# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-04 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingest', '0006_agendaitem_meeting_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='icon',
            field=models.CharField(max_length=100, null=True),
        ),
    ]