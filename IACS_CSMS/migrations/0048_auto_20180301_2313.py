# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 23:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0047_auto_20180301_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='Zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IACS_CSMS.Zone'),
        ),
    ]
