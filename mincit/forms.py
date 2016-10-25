

from django import forms
from mincit.models import Informacion, Situacion, Planeacion


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())


class InformacionForm(forms.ModelForm):
    class Meta:
        model = Informacion
        fields = [
            'nombre_empresa',
            'razon_social',
            'nombre_contacto',
            'posicion_empresa',
            'numero_tel',
            'telfono_movil',
            'tiempo_operacion',
            'productos_servicio',]
        widgets = {
            'nombre_empresa': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Nombre de la Empresa'}),
            'razon_social': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'razon social'}),
            'nombre_contacto': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'nombre de contacto'}),
            'posicion_empresa': forms.TextInput(attrs={'class': 'form-control',
                                                        'placeholder': 'posicion de la empresa'}),
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










