# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-23 22:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('futbokas', '0016_item_crt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='crt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='futbokas.Category', unique=1),
        ),
    ]