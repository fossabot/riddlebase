# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-03 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riddles', '0009_auto_20160602_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='riddlestate',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
