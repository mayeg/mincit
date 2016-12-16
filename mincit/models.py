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
    posicion_empresa = models.CharField(max_length=50,
                                        choices=POSICION_EMPRESA_CHOICE,
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
    planes_largo_p = models.CharField(max_length=250,
                                      choices=PLANES_EMPRESA_CHOICE,
                                      default='No seleccion')
    mision = models.CharField(max_length=20, choices=MISION_CHOICE,
                              default='No seleccion')
    vision = models.CharField(max_length=20, choices=VISION_CHOICE,
                              default='No seleccion')
    objetivos = models.CharField(max_length=20, choices=OBJETIVOS_CHOICE,
                                 default='No seleccion')
    estrategias = models.CharField(max_length=20, choices=ESTRATEGIAS_CHOICE,
                                   default='No seleccion')
    plan_accion = models.CharField(max_length=20, choices=PLAN_ACCION_CHOICE,
                                   default='No seleccion')
    establece_valores = models.CharField(max_length=20,
                                         choices=VALORES_EMPRESA_CHOICE,
                                         default='No seleccion')
    objetivos_largo_plazo = models.TextField()
    recursos = models.TextField()
    debilidades = models.TextField()
    oportunidades = models.TextField()
    obstaculos = models.TextField(default="")
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
    elabora_planes = models.CharField(max_length=50,
                                      choices=ELABORA_PLANES_CHOICE,
                                      default='No seleccion')
    tiempo_planeacion = models.CharField(max_length=50,
                                         choices=TIEMPO_PLANEACION_CHOICE,
                                         default='No seleccion')
    participacion_empleados = models.CharField(max_length=1,
                                               choices=PARTICIPACION_EMPLEADOS_CHOICE,
                                               default='No seleccion')
    conocen_objetivos = models.CharField(max_length=1,
                                         choices=CONOCEN_OBJETIVOS_CHOICE,
                                         default='No seleccion')
    estartegias_plan_accion = models.CharField(max_length=1,
                                               choices=ESTRATEGIAS_PLAN_ACCION_CHOICE,
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
    procesos_documentados = models.CharField(max_length=20,
                                             choices=PROCESOS_DOCUMENTADOS_CHOICE,
                                             default='No seleccion')
    evalua_procesos = models.CharField(max_length=20,
                                       choices=EVALUA_PROCESOS_CHOICE,
                                       default='No seleccion')
    automatiza_procesos = models.CharField(max_length=20,
                                           choices=AUTOMATIZA_PROCESOS_CHOICE,
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
    maximo_compromiso = models.CharField(max_length=20,
                                         choices=MAXIMO_COMPROMISO_CHOICE,
                                         default='No seleccion')
    clima_laboral = models.CharField(max_length=20,
                                     choices=CLIMA_LABORAL_CHOICE,
                                     default='No seleccion')
    motivacion_empleados = models.CharField(max_length=20,
                                            choices=MOTIVACION_EMPLEADOS_CHOICE,
                                            default='No seleccion')
    decisiones_unilaterales = models.CharField(max_length=20,
                                               choices=DECISIONES_UNILATERALES_CHOICE,
                                               default='No seleccion')
    decisiones_consenso = models.CharField(max_length=20,
                                           choices=DECISIONES_CONSENSO_CHOICE,
                                           default='No seleccion')
    define_acciones = models.CharField(max_length=20,
                                       choices=DEFINE_ACCIONES_CHOICE,
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
    sistema_control = models.CharField(max_length=20,
                                       choices=SISTEMA_CONTROL_CHOICE,
                                       default='No seleccion')
    compara_planeado = models.CharField(max_length=20,
                                        choices=COMPARA_PLANEADO_CHOICE,
                                        default='No seleccion')
    uso_indicadores = models.CharField(max_length=20,
                                       choices=USO_INDICADORES_CHOICE,
                                       default='No seleccion')
    monitoreo_indicadores = models.CharField(max_length=20,
                                             choices=MONITOREO_INDICADORES_CHOICE,
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

    ESTABLECE_RECOMPENSA_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )

    EMPLEADOS_SUFICIENTES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )

    contrata_directamente = models.CharField(max_length=20,
                                             choices=CONTRATA_DIRECTAMENTE_CHOICE,
                                             default='No seleccion')
    comibina_contratacion = models.CharField(max_length=20,
                                             choices=COMBINA_CONTRATACION_CHOICE,
                                             default='No seleccion')
    procesos_seleccion = models.CharField(max_length=20,
                                          choices=PROCESOS_SELECCION_CHOICE,
                                          default='No seleccion')
    establece_recompensa = models.CharField(max_length=20,
                                            choices=ESTABLECE_RECOMPENSA_CHOICE,
                                            default='No seleccion')
    numero_empleados = models.IntegerField()
    empleados_suficientes = models.CharField(max_length=20,
                                             choices=EMPLEADOS_SUFICIENTES_CHOICE,
                                             default='No seleccion')


class Financiera(models.Model):
    SISTEMA_CONTABILIDAD_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    CONTABILIDAD_AL_DIA_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    NORMAS_CONTABILIDAD_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    PLANIFICACION_FINANCIERA_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    MARGEN_RENTABILIDAD_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    RENTABILIDAD_POSITIVO_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    NIVEL_ENDEUDAMIENTO_CHOICE = (
        ('alto', 'Alto'),
        ('medio', 'Medio'),
        ('bajo', 'Bajo'),
        ('no conoce', 'No lo conoce'),
    )
    INGRESOS_CUMPLE_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    SUFICIENTE_CAPITAL_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    FLUJO_CAJA_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    COSTO_PRODUCTO_SERVICIO_CHOICE = (
        ('si', 'Si'),
        ('parcialmente', 'Parcialmente'),
        ('no', 'No'),
    )
    PRESUPUESTO_CHOICE = (
        ('si', 'Si'),
        ('parcialmente', 'Parcialmente'),
        ('no', 'No'),
    )
    TOMA_DECISIONES_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )

    sistema_contabilidad = models.CharField(max_length=20,
                                            choices=SISTEMA_CONTABILIDAD_CHOICE,
                                            default='No seleccion')
    contabilidad_al_dia = models.CharField(max_length=20,
                                           choices=CONTABILIDAD_AL_DIA_CHOICE,
                                           default='No seleccion')
    normas_contabilidad = models.CharField(max_length=20,
                                           choices=NORMAS_CONTABILIDAD_CHOICE,
                                           default='No seleccion')
    facturado_ultimo = models.IntegerField()
    planificacion_financiera = models.CharField(max_length=20,
                                                choices=PLANIFICACION_FINANCIERA_CHOICE,
                                                default='No seleccion')
    margen_rentabilidad = models.CharField(max_length=20,
                                           choices=MARGEN_RENTABILIDAD_CHOICE,
                                           default='No seleccion')
    rentabilidad_positivo = models.CharField(max_length=20,
                                             choices=RENTABILIDAD_POSITIVO_CHOICE,
                                             default='No seleccion')
    nivel_endeudamiento = models.CharField(max_length=20,
                                           choices=NIVEL_ENDEUDAMIENTO_CHOICE,
                                           default='No seleccion')
    ingresos_cumplen = models.CharField(max_length=20,
                                        choices=INGRESOS_CUMPLE_CHOICE,
                                        default='No seleccion')
    suficiente_capital = models.CharField(max_length=20,
                                          choices=SUFICIENTE_CAPITAL_CHOICE,
                                          default='No seleccion')
    flujo_caja = models.CharField(max_length=20,
                                  choices=FLUJO_CAJA_CHOICE,
                                  default='No seleccion')
    costo_producto_servicio = models.CharField(max_length=20,
                                               choices=COSTO_PRODUCTO_SERVICIO_CHOICE,
                                               default='No seleccion')
    presupuesto = models.CharField(max_length=20,
                                   choices=PRESUPUESTO_CHOICE,
                                   default='No seleccion')
    toma_decisiones = models.CharField(max_length=20,
                                       choices=TOMA_DECISIONES_CHOICE,
                                       default='No seleccion')


class Produccion(models.Model):
    ESTADO_MAQUINARIA_CHOICE = (
        ('excelente', 'Excelente'),
        ('muy_buena', 'Muy Buena'),
        ('buena', 'Buena'),
        ('regular', 'Regular'),
        ('obsoleta', 'Obsoleta'),
    )
    PROGRAMA_PRODUCCION_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    PRODCCION_RESPONDE_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    PROCESOS_PRODUCCION_DEFINE_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    CONTROL_CALIDAD_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    ABASTECIMIENTO_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    ADQUISISION_MAQUINARIA_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    PLANES_CONTINGENCIA_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    REALIZA_INVENTARIOS_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    HACE_SEGUIMIENTO_CHOICE = (
        ('si', 'Si'),
        ('parcialmente', 'Parcialmente'),
        ('no', 'No'),
    )
    EFICIENCIA_DISTRIBUCION_CHOICE = (
        ('si', 'Si'),
        ('parcialmente', 'Parcialmente'),
        ('no', 'No'),
    )
    porcentaje_capacidad = models.CharField(max_length=250)
    normas_tecnicas = models.CharField(max_length=250)
    estado_maquinaria = models.CharField(max_length=20,
                                         choices=ESTADO_MAQUINARIA_CHOICE,
                                         default='No seleccion')
    programa_produccion = models.CharField(max_length=20,
                                           choices=PROGRAMA_PRODUCCION_CHOICE,
                                           default='No seleccion')
    produccion_responde = models.CharField(max_length=20,
                                           choices=PRODCCION_RESPONDE_CHOICE,
                                           default='No seleccion')
    proceso_produccion_define = models.CharField(max_length=20,
                                                 choices=PROCESOS_PRODUCCION_DEFINE_CHOICE,
                                                 default='No seleccion')
    control_calidad = models.CharField(max_length=20,
                                       choices=CONTROL_CALIDAD_CHOICE,
                                       default='No seleccion')
    problemas_abastecimiento = models.CharField(max_length=20,
                                                choices=ABASTECIMIENTO_CHOICE,
                                                default='No seleccion')
    planea_adquisicion = models.CharField(max_length=20,
                                          choices=ADQUISISION_MAQUINARIA_CHOICE,
                                          default='No seleccion')
    planes_contingencia = models.CharField(max_length=20,
                                           choices=PLANES_CONTINGENCIA_CHOICE,
                                           default='No seleccion')
    realiza_inventarios = models.CharField(max_length=20,
                                           choices=REALIZA_INVENTARIOS_CHOICE,
                                           default='No seleccion')
    seguimiento_inventario = models.CharField(max_length=20,
                                              choices=HACE_SEGUIMIENTO_CHOICE,
                                              default='No seleccion')
    eficiencia_distribucion = models.CharField(max_length=20,
                                               choices=EFICIENCIA_DISTRIBUCION_CHOICE,
                                               default='No seleccion')


class Internacionalizacion(models.Model):
    paises_exportado_importado = models.TextField()
    mercados_exportado_importado = models.TextField()
    metas_relacion = models.TextField()
    estrategia_marketing = models.TextField()
    total_ventas_esperadas = models.TextField()
    margen_comercial = models.TextField()
    capital_presupuestado = models.TextField()


class AspectosAdicionales(models.Model):
    aspecto = models.CharField(max_length=250)


class PuntosPorDiagnostico(models.Model):
    punto_problematico = models.CharField(max_length=250)


class Mercadeo(models.Model):
    EXISTE_DEPARTAMENTO_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    MENSAJE_CLARO_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    DEDICA_MARKETING_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    DELEGA_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    PLAN_MERCADEO_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    IMPLEMENTA_PLAN_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    TIENE_CRONOGRAMA_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    DEFINE_PERFIL_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )
    CLIENTES_ACTIVOS_POTENCIALES_CHOICE = (
        ('si', 'Si'),
        ('no', 'No'),
    )
    PAGINA_WEB_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
        ('no tiene web', 'No Tiene Web'),
    )
    USAR_TECNOLOGIA_CHOICE = (
        ('si', 'Si'),
        ('mas o menos', 'Mas o Menos'),
        ('no', 'No'),
    )

    existe_departamento_mercadeo = models.CharField(max_length=20,
                                                    choices=EXISTE_DEPARTAMENTO_CHOICE,
                                                    default='No seleccion')

    mensaje_claro = models.CharField(max_length=20,
                                     choices=MENSAJE_CLARO_CHOICE,
                                     default='No seleccion')
    dedica_marketing_difusion = models.CharField(max_length=20,
                                                 choices=DEDICA_MARKETING_CHOICE,
                                                 default='No seleccion')
    delega = models.CharField(max_length=20, choices=DELEGA_CHOICE,
                              default='No seleccion')
    plan_mercadeo = models.CharField(max_length=20,
                                     choices=PLAN_MERCADEO_CHOICE,
                                     default='No seleccion')
    implementa_plan = models.CharField(max_length=20,
                                       choices=IMPLEMENTA_PLAN_CHOICE,
                                       default='No seleccion')
    tiene_cronograma = models.CharField(max_length=20,
                                        choices=TIENE_CRONOGRAMA_CHOICE,
                                        default='No seleccion')
    definir_perfil = models.CharField(max_length=20,
                                      choices=DEFINE_PERFIL_CHOICE,
                                      default='No seleccion')
    clientes_activos_potenciales = models.CharField(max_length=20,
                                                    choices=CLIENTES_ACTIVOS_POTENCIALES_CHOICE,
                                                    default='No seleccion')
    paginas_web = models.CharField(max_length=20, choices=PAGINA_WEB_CHOICE,
                                   default='No seleccion')
    usar_tecnologias = models.CharField(max_length=20,
                                        choices=USAR_TECNOLOGIA_CHOICE,
                                        default='No seleccion')


class DiagnosticoEmpresa(models.Model):
    fecha = models.DateField()
    numero_consecutivo = models.CharField(max_length=50)
    asesor = models.CharField(max_length=100)
    id_empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    id_situacion = models.OneToOneField(Situacion, null=True, blank=True,
                                        on_delete=models.CASCADE)
    id_planeacion = models.OneToOneField(Planeacion, null=True, blank=True,
                                         on_delete=models.CASCADE)
    id_organizacion = models.OneToOneField(Organizacion, null=True, blank=True,
                                           on_delete=models.CASCADE)
    id_direccion = models.OneToOneField(Direccion, null=True, blank=True,
                                        on_delete=models.CASCADE)
    id_control = models.OneToOneField(Control, null=True, blank=True,
                                      on_delete=models.CASCADE)
    id_recursos = models.OneToOneField(Recurso, null=True, blank=True,
                                       on_delete=models.CASCADE)
    id_mercadeo = models.IntegerField(default=0)
    id_financiera = models.OneToOneField(Financiera, null=True, blank=True,
                                         on_delete=models.CASCADE)
    id_produccion = models.OneToOneField(Produccion, null=True, blank=True,
                                         on_delete=models.CASCADE)
    id_internacionalizacion = models.OneToOneField(Internacionalizacion,
                                                   null=True,
                                                   blank=True,
                                                   on_delete=models.CASCADE)
    id_aspectos = models.OneToOneField(AspectosAdicionales, null=True,
                                       blank=True,
                                       on_delete=models.CASCADE)
    id_resumen = models.IntegerField()


class AspectosMejorarDiagnosticoEmpresa(models.Model):
    aspecto_mejorar = models.CharField(max_length=250)


class PlanAccion(models.Model):
    fecha = models.DateField()
    numero_consecutivo = models.CharField(max_length=50)
    asesor = models.CharField(max_length=100)
    id_aspecto_mejora_diagnostico_empresa = models.OneToOneField(
        AspectosMejorarDiagnosticoEmpresa, null=True, blank=True,
        on_delete=models.CASCADE)
