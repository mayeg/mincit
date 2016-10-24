

from django import forms
from mincit.models import Informacion


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput())


class InformacionForm(forms.ModelForm):
    class Meta:
        model = Informacion
        fields = (
            'nombre_empresa',
            'razon_social',
            'nombre_contacto',
            'posicion_empresa',
            'numero_tel',
            'telfono_movil',
            'tiempo_operacion',
            'productos_servicio')















