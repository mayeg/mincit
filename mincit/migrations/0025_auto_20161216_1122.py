# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-16 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mincit', '0024_auto_20161216_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosticoempresa',
            name='id_resumen',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
