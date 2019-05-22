# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-15 20:17
from __future__ import unicode_literals

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0102_auto_20180815_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditpathway',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID'),
        ),
    ]
