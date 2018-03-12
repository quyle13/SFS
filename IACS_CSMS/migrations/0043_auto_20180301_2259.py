# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 22:59
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0042_auto_20180301_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='Asset',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='Zone_Name', chained_model_field='Zone_Name', default='', on_delete=django.db.models.deletion.CASCADE, show_all=True, to='IACS_CSMS.Asset'),
        ),
    ]
