# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-28 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jys', '0005_auto_20160627_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='choice_e',
        ),
        migrations.RemoveField(
            model_name='question',
            name='choice_f',
        ),
    ]
