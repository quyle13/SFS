# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 17:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0059_auto_20180312_1743'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asset',
            old_name='DeclaredUser',
            new_name='ResponsibleUser',
        ),
        migrations.AddField(
            model_name='asset',
            name='ReviewedDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
