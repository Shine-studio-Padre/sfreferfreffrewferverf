# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 22:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbokas', '0019_item_crt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='crt',
        ),
    ]
