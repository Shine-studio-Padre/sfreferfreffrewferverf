# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('futbokas', '0024_item_crt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='crt',
        ),
    ]
