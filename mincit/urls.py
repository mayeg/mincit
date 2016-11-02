from django.conf.urls import url

from mincit import views

app_name = 'mincit'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^index/$', views.InicioListViews.as_view(), name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^diagnostico_emp/([\d+])/$', views.DiagnosticoEmpresaListViews.as_view(),
        name='diagnostico_emp'),
]
