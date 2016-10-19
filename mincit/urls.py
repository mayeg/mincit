from django.conf.urls import url

from mincit.Views import views

app_name = 'mincit'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^inicio/$', views.InicioViews.as_view(), name='inicio'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^diagnostico_emp/$', views.diagnostico_emp, name='diagnostico_emp'),


]
