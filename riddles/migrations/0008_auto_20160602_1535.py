# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-02 13:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0007_auto_20160602_1251'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='riddlestate',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='riddlestate',
            name='riddle',
        ),
        migrations.RemoveField(
            model_name='riddlestate',
            name='user',
        ),
        migrations.RemoveField(
            model_name='sudoku',
            name='riddle_type',
        ),
        migrations.DeleteModel(
            name='RiddleState',
        ),
        migrations.DeleteModel(
            name='Sudoku',
        ),
    ]
