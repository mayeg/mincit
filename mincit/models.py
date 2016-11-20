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
    id_empresa = models.OneToOneField(Empresa, null=True, blank=True,
                                          on_delete=models.CASCADE)
    razon_social = models.CharField(max_length=250)
    nombre_contacto = models.CharField(max_length=50)
    posicion_empresa = models.CharField(max_length=50, choices=POSICION_EMPRESA_CHOICE,
                                        default='No seleccion')
    numero_tel = models.IntegerField()
    telfono_movil = models.IntegerField()
    tiempo_operacion = models.IntegerField()
    productos_servicio = models.TextField()


class Situacion(models.Model):

    SECTOR_EMPRESA_CHOICE = (
        ('Agricola/Agroindustrial', 'Agricola/agroindustrial'),
        ('Sector servicios', 'Sector servicios '),
        ('Manufactura', 'Manufactura'),
        ('Comercio', 'comercio'),
    )
    PLANES_EMPRESA_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    MISION_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    VISION_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    OBJETIVOS_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    ESTRATEGIAS_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    PLAN_ACCION_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    VALORES_EMPRESA_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    sector = models.CharField(max_length=150, choices=SECTOR_EMPRESA_CHOICE,
                              default='No seleccion')
    planes_largo_p = models.CharField(max_length=250, choices=PLANES_EMPRESA_CHOICE,
                                      default='No seleccion')
    mision = models.CharField(max_length=20, choices=MISION_CHOICE, default='No seleccion')
    vision = models.CharField(max_length=20, choices=VISION_CHOICE, default='No seleccion')
    objetivos = models.CharField(max_length=20, choices=OBJETIVOS_CHOICE, default='No seleccion')
    estrategias = models.CharField(max_length=20, choices=ESTRATEGIAS_CHOICE, default='No seleccion')
    plan_accion = models.CharField(max_length=20, choices=PLAN_ACCION_CHOICE, default='No seleccion')
    establece_valores = models.CharField(max_length=20, choices=VALORES_EMPRESA_CHOICE,
                                         default='No seleccion')
    objetivos_largo_plazo = models.TextField()
    recursos = models.TextField()
    debilidades = models.TextField()
    oportunidades = models.TextField()
    obstaculos = models.TextField()
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


class DiagnosticoEmpresa(models.Model):
    fecha = models.DateField()
    numero_consecutivo = models.CharField(max_length=50)
    asesor = models.CharField(max_length=100)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_situacion = models.OneToOneField(Situacion, null=True, blank=True, on_delete=models.CASCADE)
    id_planeacion = models.OneToOneField(Planeacion, null=True, blank=True, on_delete=models.CASCADE)
    id_organizacion = models.OneToOneField(Organizacion, null=True, blank=True, on_delete=models.CASCADE)
    id_direccion = models.OneToOneField(Direccion, null=True, blank=True, on_delete=models.CASCADE)
    id_control = models.OneToOneField(Control, null=True, blank=True, on_delete=models.CASCADE)
    id_recursos = models.OneToOneField(Recurso, null=True, blank=True, on_delete=models.CASCADE)
    id_mercadeo = models.IntegerField(default=0)
    id_financiera = models.IntegerField(default=0)
    id_produccion = models.IntegerField(default=0)
    id_internacionalizacion = models.IntegerField(default=0)
    id_aspectos = models.IntegerField(default=0)
    id_resumen = models.IntegerField(default=0)
