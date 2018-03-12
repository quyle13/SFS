# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2018-02-28 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IACS_CSMS', '0007_auto_20180228_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conduit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Conduit_Name', models.CharField(default='', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Zone_Name', models.CharField(default='', max_length=500)),
                ('Zone_Type', models.CharField(choices=[('BCPS', 'Basic Control Process System Zone'), ('SIS', 'Safety Instrumented Systems Zone'), ('PIZ', 'Plant Information Zone'), ('OZ', 'Other Zone'), ('CN', 'Corporate Network'), ('DMZ', 'DMZ Zone')], default='BCPS', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='asset',
            name='Zone_Type',
        ),
        migrations.AddField(
            model_name='zone',
            name='Asset',
            field=models.ManyToManyField(default='', to='IACS_CSMS.Asset'),
        ),
    ]