# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-04-30 15:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
    ]
