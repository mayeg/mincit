

from django import forms
from django.utils.safestring import mark_safe
from mincit.models import Informacion, Situacion, Planeacion, DiagnosticoEmpresa, \
    Organizacion, Direccion, Control, Recurso


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








