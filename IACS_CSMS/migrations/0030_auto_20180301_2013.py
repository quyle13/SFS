# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-03-01 20:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0029_auto_20180301_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Risk_Name', models.CharField(default='', max_length=500)),
                ('Description', models.CharField(default='', max_length=500)),
                ('Likelihood', models.CharField(choices=[('FREQ', 'Frequent'), ('PRO', 'Probable'), ('OCC', 'Occasional'), ('REM', 'Remote'), ('IMP', 'Improbable'), ('INC', 'Incredible')], default='FREQ', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Threat_Name', models.CharField(default='', max_length=300)),
                ('Description', models.CharField(default='', max_length=500)),
                ('Source', models.CharField(choices=[('NA', 'Nation states or national governments'), ('TE', 'Terrorists'), ('IS', 'Industrial spies'), ('CG', 'Organized crime groups'), ('HK', 'Hacktivists and hackers'), ('BC', 'Business competitors'), ('DI', 'Disgruntled insiders')], default='HK', max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='RevisedDate',
        ),
        migrations.RemoveField(
            model_name='conduit',
            name='RevisedDate',
        ),
        migrations.RemoveField(
            model_name='zone',
            name='RevisedDate',
        ),
        migrations.AlterField(
            model_name='application',
            name='RegisteredDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 20, 13, 7, 724984)),
        ),
        migrations.AlterField(
            model_name='application',
            name='RevisedDate',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='RegisteredDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 20, 13, 7, 725985)),
        ),
        migrations.AlterField(
            model_name='conduit',
            name='RegisteredDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 20, 13, 7, 728987)),
        ),
        migrations.AlterField(
            model_name='zone',
            name='RegisteredDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 3, 1, 20, 13, 7, 726986)),
        ),
        migrations.AddField(
            model_name='risk',
            name='Threat',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='IACS_CSMS.Threat'),
        ),
        migrations.AddField(
            model_name='risk',
            name='Zone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IACS_CSMS.Zone'),
        ),
    ]