from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Diagnostico_Emp(models.Model):
    fecha = models.DateField()
    numero_consecutivo = models.IntegerField()
    id_informacion = models.IntegerField()
    id_situacion = models.IntegerField()
    id_planeacion = models.IntegerField()
    id_organizacion = models.IntegerField()
    id_direccion = models.IntegerField()
    id_control = models.IntegerField()
    id_recursos = models.IntegerField()
    id_mercadeo = models.IntegerField()
    id_financiera = models.IntegerField()
    id_produccion = models.IntegerField()
    id_internacionalizacion = models.IntegerField()
    id_aspectos = models.IntegerField()
    id_resumen = models.IntegerField()

class Informacion(models.Model):
    nombre_empresa = models.CharField(max_length=250)
    razon_social = models.CharField(max_length=250)
    nombre_contacto = models.CharField(max_length=50)
    posicion_empresa = models.CharField(max_length=50)
    numero_tel = models.IntegerField()
    telfono_movil = models.IntegerField()
    tiempo_operacion = models.IntegerField()
    productos_servicio = models.TextField()

