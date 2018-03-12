# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 23:01
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0044_auto_20180301_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='Asset',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='Zone_Name', chained_model_field='Zone_Name', default='', on_delete=django.db.models.deletion.CASCADE, to='IACS_CSMS.Asset'),
        ),
    ]
