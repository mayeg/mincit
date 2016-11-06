# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-05 17:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mincit', '0009_auto_20161105_1502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnosticoempresa',
            name='id_informacion',
        ),
        migrations.AddField(
            model_name='empresa',
            name='id_informacion',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mincit.Informacion'),
        ),
        migrations.AlterField(
            model_name='diagnosticoempresa',
            name='asesor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='diagnosticoempresa',
            name='id_empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mincit.Empresa'),
        ),
    ]
