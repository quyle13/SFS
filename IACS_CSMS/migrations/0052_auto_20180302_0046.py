# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-02 00:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0051_auto_20180301_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='risk',
            name='Likelihood',
            field=models.CharField(choices=[('FREQ', 'Frequent - Many times in system lifetime (Range > 10^-3)'), ('PRO', 'Probable - Several times in system lifetime (10^-3 < Range <  10^-4)'), ('OCC', 'Occasional - Once in system lifetime (10^-4 < Range < 10^-5)'), ('REM', 'Remote - Unlikely in system lifetime (10^-5 < Range < 10^-6) '), ('IMP', 'Improbable - Very unlikely to occur (10^-6 < Range < 10^-7)'), ('INC', 'Incredible - Cannot believe that it could occur (Range < 10^-7)')], default='FREQ', max_length=50),
        ),
    ]
