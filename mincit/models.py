from __future__ import unicode_literals
from django.db import models


class Empresa(models.Model):
    nombre = models.CharField(max_length=250, unique=True)
    nit = models.CharField(max_length=50, unique=True)


class Informacion(models.Model):
    POSICION_EMPRESA_CHOICE = (
        ('representante_legal', 'Representante Legal'),
        ('socio', 'Socio'),
        ('otro', 'Otro'),
    )
    nombre_empresa = models.CharField(max_length=250)
    razon_social = models.CharField(max_length=250)
    nombre_contacto = models.CharField(max_length=50)
    posicion_empresa = models.CharField(max_length=50, choices=POSICION_EMPRESA_CHOICE,
                                        default='No seleccion')
    numero_tel = models.IntegerField()
    telfono_movil = models.IntegerField()
    tiempo_operacion = models.IntegerField()
    productos_servicio = models.TextField()


class Situacion(models.Model):
    sector = models.CharField(max_length=150)
    planes_largo_p = models.CharField(max_length=250)
    mision = models.CharField(max_length=1)
    vision = models.CharField(max_length=1)
    objetivos = models.CharField(max_length=1)
    estrategias = models.CharField(max_length=1)
    plan_accion = models.CharField(max_length=1)
    establece_valores = models.TextField()
    objetivos_largo_p = models.TextField()
    recursos = models.TextField()
    debilidades = models.TextField()
    oportunidades = models.TextField()
    ventaja_empresa = models.TextField()
    ventaja_competencia = models.TextField()


class Planeacion(models.Model):
    elabora_planes = models.CharField(max_length=50)
    tiempo_planeacion = models.CharField(max_length=50)
    participacion_empleados = models.CharField(max_length=1)
    conocen_objetivos = models.CharField(max_length=1)
    estartegias_plan_accion = models.CharField(max_length=1)


class Organizacion(models.Model):
    organigrama = models.CharField(max_length=1)
    procesos_documentados = models.CharField(max_length=1)
    evalua_procesos = models.CharField(max_length=1)
    automatiza_procesos = models.CharField(max_length=1)


class Direccion(models.Model):
    maximo_compromiso = models.CharField(max_length=1)
    clima_laboral = models.CharField(max_length=1)
    motivacion_empleados = models.CharField(max_length=1)
    decisiones_unilaterales = models.CharField(max_length=1)
    decisiones_consenso = models.CharField(max_length=1)
    define_acciones = models.CharField(max_length=1)


class Control(models.Model):
    sistema_control = models.CharField(max_length=1)
    compara_planeado = models.CharField(max_length=1)
    uso_indicadores = models.CharField(max_length=1)
    monitoreo_indicadores = models.CharField(max_length=1)


class Recurso(models.Model):
    contrata_directamente = models.CharField(max_length=1)
    comibina_contratacion = models.CharField(max_length=1)
    procesos_seleccion = models.CharField(max_length=1)
    numero_empleados = models.IntegerField()
    empleados_suficientes = models.CharField(max_length=1)


class Diagnostico_Emp(models.Model):
    fecha = models.DateField()
    numero_consecutivo = models.IntegerField()
    asesor = models.CharField(max_length=100, default="")
    id_empresa = models.ForeignKey(Empresa, default="", on_delete=models.CASCADE)
    id_informacion = models.OneToOneField(Informacion, on_delete=models.CASCADE)
    id_situacion = models.OneToOneField(Situacion, on_delete=models.CASCADE)
    id_planeacion = models.OneToOneField(Planeacion, on_delete=models.CASCADE)
    id_organizacion = models.OneToOneField(Organizacion, on_delete=models.CASCADE)
    id_direccion = models.OneToOneField(Direccion, on_delete=models.CASCADE)
    id_control = models.OneToOneField(Control, on_delete=models.CASCADE)
    id_recursos = models.OneToOneField(Recurso, on_delete=models.CASCADE)
    id_mercadeo = models.IntegerField()
    id_financiera = models.IntegerField()
    id_produccion = models.IntegerField()
    id_internacionalizacion = models.IntegerField()
    id_aspectos = models.IntegerField()
    id_resumen = models.IntegerField()
