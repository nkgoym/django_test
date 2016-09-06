# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-22 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice_Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_content', models.TextField(blank=True, null=True)),
                ('choice_content', models.CharField(max_length=500)),
                ('correct_choice', models.CharField(max_length=4)),
            ],
        ),
    ]
