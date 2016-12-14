# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-09 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('mincit', '0012_auto_20161106_1235'),
    ]

    operations = [
        migrations.RenameField(
            model_name='situacion',
            old_name='objetivos_largo_p',
            new_name='objetivos_largo_plazo',
        ),
        migrations.AlterField(
            model_name='situacion',
            name='establece_valores',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='estrategias',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='mision',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='objetivos',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='plan_accion',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='planes_largo_p',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=250),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='sector',
            field=models.CharField(
                choices=[('Agricola/Agroindustrial', 'Agricola/agroindustrial'),
                         ('Sector servicios', 'Sector servicios '),
                         ('Manufactura', 'Manufactura'),
                         ('Comercio', 'comercio')], default='No seleccion',
                max_length=150),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='vision',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')],
                                   default='No seleccion', max_length=20),
        ),
    ]
