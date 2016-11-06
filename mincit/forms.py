

from django import forms
from django.utils.safestring import mark_safe
from mincit.models import Informacion, Situacion, Planeacion, DiagnosticoEmpresa


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
            'objetivos_largo_p',
            'recursos',
            'debilidades',
            'oportunidades',
            'ventaja_empresa',
            'ventaja_competencia',
        ]

        widgets = {
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
                    }










