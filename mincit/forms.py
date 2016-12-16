

from django import forms
from django.utils.safestring import mark_safe
from mincit.models import Informacion, Situacion, Planeacion, DiagnosticoEmpresa, \
    Organizacion, Direccion, Control, Recurso, Financiera, Produccion, \
    Internacionalizacion, Mercadeo


class HorizontalRadioRenderer(forms.RadioSelect.renderer):
  def render(self):
    return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())


class DiagnosticoEmpresaForm(forms.ModelForm):
    class Meta:
        model = DiagnosticoEmpresa
        fields = [
            'fecha',
            'numero_consecutivo',
            'asesor',
            'id_empresa',
            'id_situacion',
            'id_planeacion',
            'id_organizacion',
            'id_direccion',
            'id_control',
            'id_recursos',
            'id_mercadeo',
            'id_financiera',
            'id_produccion',
            'id_internacionalizacion',
            'id_aspectos',
            'id_resumen',
        ]


class InformacionForm(forms.ModelForm):
    class Meta:
        model = Informacion
        fields = [
            'razon_social',
            'nombre_contacto',
            'posicion_empresa',
            'numero_tel',
            'telfono_movil',
            'tiempo_operacion',
            'productos_servicio',
        ]
        widgets = {
            'razon_social': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'razon social'}),
            'nombre_contacto': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'nombre de contacto'}),
            'posicion_empresa': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'numero_tel': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'numero de telefono',
                                                 'type': 'number'}),
            'telefono_movil': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'telefono',
                                                 'type': 'number'}),
            'tiempo_operacion': forms.TextInput(attrs={'class': 'form-control',
                                                 'placeholder': 'tiempo de operacion',
                                                 'type': 'number'}),
            'productos_servicio': forms.Textarea(
                attrs={'class': 'form-control',  'placeholder': 'productos y servicios',
                       'rows': 3}),
        }


class SituacionForm(forms.ModelForm):
    class Meta:
        model = Situacion
        fields = [
            'sector',
            'planes_largo_p',
            'mision',
            'vision',
            'objetivos',
            'estrategias',
            'plan_accion',
            'establece_valores',
            'objetivos_largo_plazo',
            'recursos',
            'debilidades',
            'oportunidades',
            'obstaculos',
            'ventaja_empresa',
            'ventaja_competencia',
        ]

        widgets = {
            'sector': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'planes_largo_p': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'mision': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'vision': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'objetivos': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'estrategias': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'plan_accion': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'establece_valores': forms.RadioSelect(renderer=HorizontalRadioRenderer),
            'objetivos_largo_plazo': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Objetivos a largo plazo',
                       'rows': 3}),
            'recursos': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Recursos',
                       'rows': 3}),

            'debilidades': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'debilidades',
                       'rows': 3}),

            'oportunidades': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Oportunidades',
                       'rows': 3}),

            'obstaculos': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Obstaculos',
                       'rows': 3}),

            'ventaja_empresa': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Ventajas de la empresa',
                       'rows': 3}),

            'ventaja_competencia': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Ventaja de la competencia',
                       'rows': 3}),
        }


class PlaneacionForm(forms.ModelForm):
    class Meta:
        model = Planeacion
        fields = [
            'elabora_planes',
            'tiempo_planeacion',
            'participacion_empleados',
            'conocen_objetivos',
            'estartegias_plan_accion',
        ]

        widgets = {
            'elabora_planes': forms.RadioSelect(),
            'tiempo_planeacion': forms.RadioSelect(),
            'participacion_empleados': forms.RadioSelect(),
            'conocen_objetivos': forms.RadioSelect(),
            'estrategias_plan_accion': forms.RadioSelect(),
        }


class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion

        fields = [
            'organigrama',
            'procesos_documentados',
            'evalua_procesos',
            'automatiza_procesos',
        ]

        widgets = {
            'organigrama': forms.RadioSelect(),
            'procesos_documentados': forms.RadioSelect(),
            'evalua_procesos': forms.RadioSelect(),
            'automatiza_procesos': forms.RadioSelect(),
        }


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = [
            'maximo_compromiso',
            'clima_laboral',
            'motivacion_empleados',
            'decisiones_unilaterales',
            'decisiones_consenso',
            'define_acciones',
        ]

        widgets = {
            'maximo_compromiso': forms.RadioSelect(),
            'clima_laboral': forms.RadioSelect(),
            'motivacion_empleados': forms.RadioSelect(),
            'decisiones_unilaterales': forms.RadioSelect(),
            'decisiones_consenso': forms.RadioSelect(),
            'define_acciones': forms.RadioSelect(),
        }


class ControlForm(forms.ModelForm):
    class Meta:
        model = Control

        fields = [
            'sistema_control',
            'compara_planeado',
            'uso_indicadores',
            'monitoreo_indicadores',
        ]
        widgets = {
            'sistema_control': forms.RadioSelect(),
            'compara_planeado': forms.RadioSelect(),
            'uso_indicadores': forms.RadioSelect(),
            'monitoreo_indicadores': forms.RadioSelect(),
        }


class RecursoForm(forms.ModelForm):
    class Meta:
        model = Recurso

        fields = [
            'contrata_directamente',
            'comibina_contratacion',
            'procesos_seleccion',
            'establece_recompensa',
            'numero_empleados',
            'empleados_suficientes',
        ]
        widgets = {
            'contrata_directamente': forms.RadioSelect(),
            'comibina_contratacion': forms.RadioSelect(),
            'procesos_seleccion': forms.RadioSelect(),
            'establece_recompensa': forms.RadioSelect(),
            'numero_empleados': forms.NumberInput(),
            'empleados_suficientes': forms.RadioSelect(),
        }

class MercadeoForm(forms.ModelForm):
    class Meta:
        model = Mercadeo

        fields = [

            'existe_departamento_mercadeo',
            'mensaje_claro',
            'dedica_marketing_difusion',
            'delega',
            'plan_mercadeo',
            'implementa_plan',
            'tiene_cronograma',
            'definir_perfil',
            'clientes_activos_potenciales',
            'paginas_web',
            'usar_tecnologias',
        ]
        widgets = {
            'existe_departamento_mercadeo': forms.RadioSelect(),
            'mensaje_claro': forms.RadioSelect(),
            'dedica_marketing_difusion': forms.RadioSelect(),
            'delega': forms.RadioSelect(),
            'plan_mercadeo': forms.RadioSelect(),
            'implementa_plan': forms.RadioSelect(),
            'tiene_cronograma': forms.RadioSelect(),
            'definir_perfil': forms.RadioSelect(),
            'clientes_activos_potenciales': forms.RadioSelect(),
            'paginas_web': forms.RadioSelect(),
            'usar_tecnologias': forms.RadioSelect(),
        }


class FinancieraForm(forms.ModelForm):
    class Meta:
        model = Financiera

        fields = [
            'sistema_contabilidad',
            'contabilidad_al_dia',
            'normas_contabilidad',
            'facturado_ultimo',
            'planificacion_financiera',
            'margen_rentabilidad',
            'rentabilidad_positivo',
            'nivel_endeudamiento',
            'ingresos_cumplen',
            'suficiente_capital',
            'flujo_caja',
            'costo_producto_servicio',
            'presupuesto',
            'toma_decisiones',
        ]
        widgets = {
            'sistema_contabilidad': forms.RadioSelect(),
            'contabilidad_al_dia': forms.RadioSelect(),
            'normas_contabilidad': forms.RadioSelect(),
            'facturado_ultimo': forms.NumberInput(),
            'planificacion_financiera': forms.RadioSelect(),
            'margen_rentabilidad': forms.RadioSelect(),
            'rentabilidad_positivo': forms.RadioSelect(),
            'nivel_endeudamiento': forms.RadioSelect(),
            'ingresos_cumplen': forms.RadioSelect(),
            'esuficiente_capital': forms.RadioSelect(),
            'costo_producto_servicio': forms.RadioSelect(),
            'presupuesto': forms.RadioSelect(),
            'toma_decisiones': forms.RadioSelect(),
        }

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion

        fields = [
            'porcentaje_capacidad',
            'normas_tecnicas',
            'estado_maquinaria',
            'programa_produccion',
            'produccion_responde',
            'proceso_produccion_define',
            'control_calidad',
            'problemas_abastecimiento',
            'planea_adquisicion',
            'planes_contingencia',
            'realiza_inventarios',
            'seguimiento_inventario',
            'eficiencia_distribucion',
        ]

        widgets = {

            'porcentaje_capacidad': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Porcentaje de'
                                                               'capacidad'}),
            'normas_tecnicas': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Normas Tecnicas'}),
            'estado_maquinaria': forms.RadioSelect(),
            'programa_produccion': forms.RadioSelect(),
            'produccion_responde': forms.RadioSelect(),
            'proceso_produccion_define': forms.RadioSelect(),
            'control_calidad': forms.RadioSelect(),
            'problemas_abastecimiento': forms.RadioSelect(),
            'planea_adquisicion': forms.RadioSelect(),
            'planes_contingencia': forms.RadioSelect(),
            'realiza_inventarios': forms.RadioSelect(),
            'seguimiento_inventario': forms.RadioSelect(),
            'eficiencia_distribucion': forms.RadioSelect(),
        }


class InternacionalizacionForm(forms.ModelForm):
    class Meta:
        model = Internacionalizacion

        fields = [
            'paises_exportado_importado',
            'mercados_exportado_importado',
            'metas_relacion',
            'estrategia_marketing',
            'total_ventas_esperadas',
            'margen_comercial',
            'capital_presupuestado',
        ]

        widgets = {

        'paises_exportado_importado': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),
        'mercados_exportado_importado': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),

        'metas_relacion': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),

        'estrategia_marketing': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),

        'total_ventas_esperadas': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),

        'margen_comercial': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),

        'capital_presupuestado': forms.Textarea(
            attrs={'class': 'form-control',
                   'rows': 3}),

    }







