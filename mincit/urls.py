from django.conf.urls import url

from mincit import views

app_name = 'mincit'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^index/$', views.InicioListViews.as_view(), name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^diagnostico_emp/$', views.Diagnostico_empViews.as_view(),
        name='diagnostico_emp'),
    url(r'^diagnostico_emp/informacion$', views.InformacionViews.as_view(),
        name='informacion'),
    url(r'^diagnostico_emp/situacion$', views.SituacionViews.as_view(),
        name='situacion'),
    url(r'^diagnostico_emp/planeacio$', views.PlaneacionViews.as_view(),
        name='planeacion'),


]
