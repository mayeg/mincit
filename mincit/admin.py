from django.contrib import admin
from models import DiagnosticoEmpresa, Recurso
from models import Informacion, Direccion
from models import Situacion, Control
from models import Planeacion, Organizacion, Empresa, Financiera

# Register your models here.
admin.site.register(DiagnosticoEmpresa)
admin.site.register(Informacion)
admin.site.register(Situacion)
admin.site.register(Planeacion)
admin.site.register(Organizacion)
admin.site.register(Recurso)
admin.site.register(Direccion)
admin.site.register(Control)
admin.site.register(Empresa)
admin.site.register(Financiera)




