# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 18:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0004_auto_20160518_1128'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sudoku',
            old_name='type',
            new_name='riddle_type',
        ),
    ]
