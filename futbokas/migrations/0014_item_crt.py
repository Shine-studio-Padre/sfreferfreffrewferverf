# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 21:58
from __future__ import unicode_literals

import builtins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbokas', '0013_remove_item_crt'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='crt',
            field=models.ForeignKey(default=builtins.id, on_delete=django.db.models.deletion.CASCADE, to='futbokas.Category'),
            preserve_default=False,
        ),
    ]
