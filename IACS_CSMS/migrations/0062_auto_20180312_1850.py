# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 18:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0061_auto_20180312_1809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risk',
            old_name='Assessment_review_date',
            new_name='Reviewed_date',
        ),
    ]
