# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 22:17
from __future__ import unicode_literals

import IACS_CSMS.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0035_auto_20180301_2132'),
    ]

    operations = [
        migrations.RenameField(
            model_name='risk',
            old_name='RevisedDate',
            new_name='Assessment_review_date',
        ),
        migrations.RenameField(
            model_name='risk',
            old_name='RegisteredDate',
            new_name='Date_of_risk_assessment',
        ),
        migrations.AlterField(
            model_name='application',
            name='RevisedDate',
            field=models.DateTimeField(default=IACS_CSMS.models.one_day_hence, null=True),
        ),
    ]
