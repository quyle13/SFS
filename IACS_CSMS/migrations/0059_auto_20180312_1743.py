# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-12 17:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0058_application_reviewed_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='Licensed',
            new_name='License',
        ),
    ]
