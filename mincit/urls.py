from django.conf.urls import url

from mincit import views

app_name = 'mincit'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^index/$', views.InicioListViews.as_view(), name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^diagnostico_emp/([\d+])/$', views.DiagnosticoEmpresaListViews.as_view(),
        name='diagnostico_emp'),
    url(r'^diagnostico_emp/([\d+])/crear/$', views.DiagnosticoEmpresaCreateViews.as_view(),
        name='diagnostico_empresa_crear'),
    url(r'^diagnostico_emp/editar/(?P<id_diagnostico>[\d+])/$', views.DiagnosticoEmpresaUpdateViews.as_view(),
        name='editar_diagnostico'),
    url(r'^diagnostico_emp/informacion/([\d+])/$', views.InformacionViews.as_view(),
        name='informacion'),
    url(r'^diagnostico_emp/informacion/crear/([\d+])/$', views.InformacionCreateViews.as_view(),
        name='crear_informacion'),
    url(r'^diagnostico_emp/informacion/editar/(?P<id_informacion>[\d+])/$', views.InformacionUpdateViews.as_view(),
        name='editar_informacion'),
    url(r'^diagnostico_emp/situacion/([\d+])/$', views.SituacionViews.as_view(),
        name='situacion'),
    url(r'^diagnostico_emp/situacion/crear/([\d+])/$', views.InformacionCreateViews.as_view(),
        name='crear_situacion'),
    url(r'^diagnostico_emp/situacion/editar/(?P<id_situacion>[\d+])/$', views.InformacionUpdateViews.as_view(),
        name='editar_Situacion'),
    url(r'^diagnostico_emp/planeacion$', views.PlaneacionViews.as_view(),
        name='planeacion'),
]
