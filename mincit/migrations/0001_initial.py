# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostico_Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('numero_consecutivo', models.IntegerField()),
                ('id_informacion', models.IntegerField()),
                ('id_situacion', models.IntegerField()),
                ('id_planeacion', models.IntegerField()),
                ('id_organizacion', models.IntegerField()),
                ('id_direccion', models.IntegerField()),
                ('id_control', models.IntegerField()),
                ('id_recursos', models.IntegerField()),
                ('id_mercadeo', models.IntegerField()),
                ('id_financiera', models.IntegerField()),
                ('id_produccion', models.IntegerField()),
                ('id_internacionalizacion', models.IntegerField()),
                ('id_aspectos', models.IntegerField()),
                ('id_resumen', models.IntegerField()),
            ],
        ),
    ]
