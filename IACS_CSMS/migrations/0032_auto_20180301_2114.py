# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 21:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0031_auto_20180301_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='threat',
            name='Source',
        ),
        migrations.AlterField(
            model_name='threat',
            name='Threat_Name',
            field=models.CharField(choices=[('SE', 'Social Engineering'), ('PH', 'Phishing'), ('MW', 'Malware'), ('UACC', 'Unauthorised access'), ('UA', 'Unauthorised actions'), ('UD', 'Unauthorised data transfer')], default='MW', max_length=100),
        ),
    ]
