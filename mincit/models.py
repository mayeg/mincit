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
    ELABORA_PLANES_CHOICE = (
        ('semanales', 'Semanales'),
        ('mensuales', 'Mensuales'),
        ('trimestrales', 'Trimestrales'),
        ('semestrales', 'Semestrales'),
        ('anuales', 'Anuales'),
        ('largo_plazo', 'Largo Plazo'),
    )
    TIEMPO_PLANEACION_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    PARTICIPACION_EMPLEADOS_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    CONOCEN_OBJETIVOS_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    ESTRATEGIAS_PLAN_ACCION_CHOICE = (
        ('1', 'Si'),
        ('0', 'No'),
    )
    elabora_planes = models.CharField(max_length=50, choices=ELABORA_PLANES_CHOICE,
                                      default='No seleccion')
    tiempo_planeacion = models.CharField(max_length=50, choices=TIEMPO_PLANEACION_CHOICE,
                                         default='No seleccion')
    participacion_empleados = models.CharField(max_length=1, choices=PARTICIPACION_EMPLEADOS_CHOICE,
                                               default='No seleccion')
    conocen_objetivos = models.CharField(max_length=1, choices=CONOCEN_OBJETIVOS_CHOICE,
                                         default='No seleccion')
    estartegias_plan_accion = models.CharField(max_length=1, choices=ESTRATEGIAS_PLAN_ACCION_CHOICE,
                                               default='No seleccion')


class Organizacion(models.Model):
    ORGANIGRAMA_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    PROCESOS_DOCUMENTADOS_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    EVALUA_PROCESOS_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    AUTOMATIZA_PROCESOS_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    organigrama = models.CharField(max_length=29, choices=ORGANIGRAMA_CHOICE,
                                   default='No seleccion')
    procesos_documentados = models.CharField(max_length=20, choices=PROCESOS_DOCUMENTADOS_CHOICE,
                                             default='No seleccion')
    evalua_procesos = models.CharField(max_length=20, choices=EVALUA_PROCESOS_CHOICE,
                                       default='No seleccion')
    automatiza_procesos = models.CharField(max_length=20, choices=AUTOMATIZA_PROCESOS_CHOICE,
                                           default='No seleccion')


class Direccion(models.Model):
    MAXIMO_COMPROMISO_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    CLIMA_LABORAL_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    MOTIVACION_EMPLEADOS_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    DECISIONES_UNILATERALES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    DECISIONES_CONSENSO_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    DEFINE_ACCIONES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    maximo_compromiso = models.CharField(max_length=20, choices=MAXIMO_COMPROMISO_CHOICE,
                                         default='No seleccion')
    clima_laboral = models.CharField(max_length=20, choices=CLIMA_LABORAL_CHOICE,
                                     default='No seleccion')
    motivacion_empleados = models.CharField(max_length=20, choices=MOTIVACION_EMPLEADOS_CHOICE,
                                            default='No seleccion')
    decisiones_unilaterales = models.CharField(max_length=20, choices=DECISIONES_UNILATERALES_CHOICE,
                                               default='No seleccion')
    decisiones_consenso = models.CharField(max_length=20, choices=DECISIONES_CONSENSO_CHOICE,
                                           default='No seleccion')
    define_acciones = models.CharField(max_length=20, choices=DEFINE_ACCIONES_CHOICE,
                                       default='No seleccion')


class Control(models.Model):
    SISTEMA_CONTROL_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    COMPARA_PLANEADO_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    USO_INDICADORES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    MONITOREO_INDICADORES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    sistema_control = models.CharField(max_length=20, choices=SISTEMA_CONTROL_CHOICE,
                                       default='No seleccion')
    compara_planeado = models.CharField(max_length=20, choices=COMPARA_PLANEADO_CHOICE,
                                        default='No seleccion')
    uso_indicadores = models.CharField(max_length=20, choices=USO_INDICADORES_CHOICE,
                                       default='No seleccion')
    monitoreo_indicadores = models.CharField(max_length=20, choices=MONITOREO_INDICADORES_CHOICE,
                                             default='No seleccion')


class Recurso(models.Model):
    CONTRATA_DIRECTAMENTE_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    COMBINA_CONTRATACION_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    PROCESOS_SELECCION_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    EMPLEADOS_SUFICIENTES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )

    contrata_directamente = models.CharField(max_length=20, choices=CONTRATA_DIRECTAMENTE_CHOICE,
                                             default='No seleccion')
    comibina_contratacion = models.CharField(max_length=20, choices=COMBINA_CONTRATACION_CHOICE,
                                             default='No seleccion')
    procesos_seleccion = models.CharField(max_length=20, choices=PROCESOS_SELECCION_CHOICE,
                                          default='No seleccion')
    numero_empleados = models.IntegerField()
    empleados_suficientes = models.CharField(max_length=20, choices=EMPLEADOS_SUFICIENTES_CHOICE,
                                             default='No seleccion')


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
