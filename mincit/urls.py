from django.conf.urls import url

from mincit.Views import views, inicioView

app_name = 'mincit'

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^inicio/$', inicioView.InicioViews.as_view(), name='inicio'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),


]
