# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mincit', '0015_auto_20161117_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='control',
            name='compara_planeado',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='control',
            name='monitoreo_indicadores',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='control',
            name='sistema_control',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='control',
            name='uso_indicadores',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='clima_laboral',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='decisiones_consenso',
            field=models.CharField(choices=[('si', 'Si'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='decisiones_unilaterales',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='define_acciones',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='maximo_compromiso',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='direccion',
            name='motivacion_empleados',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='automatiza_procesos',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='evalua_procesos',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='organigrama',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=29),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='procesos_documentados',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='planeacion',
            name='conocen_objetivos',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')], default='No seleccion', max_length=1),
        ),
        migrations.AlterField(
            model_name='planeacion',
            name='elabora_planes',
            field=models.CharField(choices=[('semanales', 'Semanales'), ('mensuales', 'Mensuales'), ('trimestrales', 'Trimestrales'), ('semestrales', 'Semestrales'), ('anuales', 'Anuales'), ('largo_plazo', 'Largo Plazo')], default='No seleccion', max_length=50),
        ),
        migrations.AlterField(
            model_name='planeacion',
            name='estartegias_plan_accion',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')], default='No seleccion', max_length=1),
        ),
        migrations.AlterField(
            model_name='planeacion',
            name='participacion_empleados',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')], default='No seleccion', max_length=1),
        ),
        migrations.AlterField(
            model_name='planeacion',
            name='tiempo_planeacion',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')], default='No seleccion', max_length=50),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='comibina_contratacion',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='contrata_directamente',
            field=models.CharField(choices=[('si', 'Si'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='empleados_suficientes',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='procesos_seleccion',
            field=models.CharField(choices=[('si', 'Si'), ('mas o menos', 'Mas o Menos'), ('no', 'No')], default='No seleccion', max_length=20),
        ),
        migrations.AlterField(
            model_name='situacion',
            name='establece_valores',
            field=models.CharField(choices=[('1', 'Si'), ('0', 'No')], default='No seleccion', max_length=20),
        ),
    ]