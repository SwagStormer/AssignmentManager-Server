# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 19:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bell', '0002_auto_20170902_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='normal_schedule_active',
            new_name='schedule_active',
        ),
    ]