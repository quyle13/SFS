# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-02 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0052_auto_20180302_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='Risk_Name',
            field=models.CharField(default='', max_length=500, unique=True),
        ),
    ]