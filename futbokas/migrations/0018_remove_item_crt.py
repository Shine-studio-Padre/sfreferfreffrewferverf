# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 22:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbokas', '0017_auto_20170924_0302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='crt',
        ),
    ]
