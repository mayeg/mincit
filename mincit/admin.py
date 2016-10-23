from django.contrib import admin
from models import Diagnostico_Emp, Recurso
from models import Informacion, Direccion
from models import Situacion, Control
from models import Planeacion, Organizacion

# Register your models here.
admin.site.register(Diagnostico_Emp)
admin.site.register(Informacion)
admin.site.register(Situacion)
admin.site.register(Planeacion)
admin.site.register(Organizacion)
admin.site.register(Recurso)
admin.site.register(Direccion)
admin.site.register(Control)





