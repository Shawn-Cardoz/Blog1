# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-01 08:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0004_auto_20161001_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 1, 8, 24, 53, 270339, tzinfo=utc)),
        ),
    ]
