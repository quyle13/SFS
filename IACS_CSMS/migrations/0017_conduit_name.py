# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-02-28 23:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0016_conduit_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='conduit',
            name='Name',
            field=models.CharField(default='', max_length=500),
        ),
    ]