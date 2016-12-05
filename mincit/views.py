from __future__ import print_function
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import response
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from django.views.generic import View, CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from mincit.forms import LoginForm, InformacionForm, SituacionForm, PlaneacionForm, DiagnosticoEmpresaForm
from models import Empresa, Informacion, DiagnosticoEmpresa, Situacion, Planeacion
from datetime import datetime


# Create your views here.


class LoginView(View):
    form = LoginForm()
    message = None
    template = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('mincit:index')
        return render(request, self.template, self.get_contex())

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login_django(request, user)
            return redirect('mincit:index')
        else:
            self.message = 'error, datos incorrectos'

        return render(request, self.template, self.get_contex())


    def get_contex(self):
        return {'form': self.form, 'message': self.message}


class InicioListViews(LoginRequiredMixin, ListView):
    login_url = 'mincit:login'
    model = Empresa
    template_name = 'index.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(InicioListViews, self).get_context_data(
            **kwargs)
        return context


@login_required(login_url='mincit:login')
def logout(request):
    logout_django(request)
    return redirect('mincit:login')


class DiagnosticoEmpresaListViews(LoginRequiredMixin, ListView):
    login_url = 'mincit:login'
    model = DiagnosticoEmpresa
    template_name = 'diagnostico_emp/diagnostico_emp.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoEmpresaListViews, self).get_context_data(**kwargs)
        self.empresa = get_object_or_404(Empresa, id=self.args[0])
        context['id_empresa'] = self.empresa.id
        return context

    def get_queryset(self):
        self.empresa = get_object_or_404(Empresa, id=self.args[0])
        return DiagnosticoEmpresa.objects.filter(id_empresa=self.empresa)


class DiagnosticoEmpresaCreateViews(LoginRequiredMixin, CreateView):
    login_url = 'mincit:login'
    model = DiagnosticoEmpresa
    form_class = DiagnosticoEmpresaForm
    template_name = 'diagnostico_emp/diagnostico_emp_crear.html'
    messages = None
    context = {
        'form': form_class
    }

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoEmpresaCreateViews, self).get_context_data(
            **kwargs)
        empresa = Empresa.objects.get(id=self.args[0])
        fecha = datetime.today()
        asesor = self.user.username
        numero = self.get_numero_diagnostico(empresa)
        diagnotico = DiagnosticoEmpresa.objects.create(id_empresa=empresa,
                                                asesor=asesor, fecha=fecha,
                                                numero_consecutivo=numero)
        context['diag'] = diagnotico
        context['id_diag'] = diagnotico.id
        return context

    def get_numero_diagnostico(self):
        # DiagnosticoEmpresa.objects. consultar los diagnosticos de la empresa
        #  ordenarlos por numero descendente y obtener solo el primer
        # resultado. return obj.numero != none + 1 si es none 1
        pass


class DiagnosticoEmpresaUpdateViews(LoginRequiredMixin, UpdateView):
    login_url = 'mincit:login'
    model = DiagnosticoEmpresa
    form_class = DiagnosticoEmpresaForm
    template_name = 'diagnostico_emp/diagnostico_emp_editar.html'
    success_url = reverse_lazy('mincit:diganostico_emp')
    slug_field = 'id'
    slug_url_kwarg = 'id_diagnostico'
    messages = None
    context = {
        'form': form_class
    }

    def get_context_data(self, **kwargs):
        context = super(DiagnosticoEmpresaUpdateViews, self).get_context_data(
            **kwargs)
        diagnostico = get_object_or_404(DiagnosticoEmpresa, id=self.kwargs['id_diagnostico'])
        print(diagnostico.id, 'id diagnostico')
        context['id_diag'] = diagnostico.id
        return context


class InformacionViews(LoginRequiredMixin, View):
    form = InformacionForm
    model = Informacion
    login_url = 'mincit:login'
    messages = None
    template = 'empresa/informacion.html'

    def get(self, request, *args, **kwargs):
        try:
            self.empresa = get_object_or_404(Empresa, id=self.args[0])
            self.informacion = Informacion.objects.get(id_empresa=self.empresa)
            return redirect('mincit:editar_informacion', self.informacion.id)
        except Informacion.DoesNotExist:
            return redirect('mincit:crear_informacion', self.empresa.id)


class InformacionCreateViews(LoginRequiredMixin, CreateView):
    model = Informacion
    form_class = InformacionForm
    template_name = 'empresa/informacion.html'
    success_url = reverse_lazy('mincit:index')
    messages = None
    context = {
        'form': form_class
    }

    def form_valid(self, form):
        empresa = Empresa.objects.get(id=self.args[0])
        form.instance.id_empresa = empresa
        return super(InformacionCreateViews, self).form_valid(form)


class InformacionUpdateViews(LoginRequiredMixin, UpdateView):
    model = Informacion
    form_class = InformacionForm
    template_name = 'empresa/informacion.html'
    success_url = reverse_lazy('mincit:index')
    slug_field = 'id'
    slug_url_kwarg = 'id_informacion'
    messages = None
    context = {
        'form': form_class
    }


class SituacionViews(LoginRequiredMixin, View):
    form = SituacionForm
    model = Situacion
    login_url = 'mincit:login'
    messages = None
    template = 'diagnostico_emp/situacion.html'

    def get(self, request, *args, **kwargs):
        self.diagnostico = get_object_or_404(
            DiagnosticoEmpresa, id=self.kwargs['id_diagnostico'])
        if self.diagnostico.id_situacion is not None:
            return redirect('mincit:editar_situacion',
                            id_situacion=self.diagnostico.id_situacion.id)

        return redirect('mincit:crear_situacion', self.diagnostico.id)


class SituacionCreateViews(LoginRequiredMixin, CreateView):
    model = Situacion
    form_class = SituacionForm
    template_name = 'diagnostico_emp/situacion_crear.html'
    messages = None
    context = {
        'form': form_class
    }
    success_url = None

    def get_success_url(self):
        diagnostico = DiagnosticoEmpresa.objects.get(
            id=self.kwargs['id_diagnostico'])
        url_reverse = "mincit:planeacion"
        try:
            diagnostico.id_situacion = self.object
            diagnostico.save()
        except DiagnosticoEmpresa.DoesNotExist:
            url_reverse = 'mincit:situacion'
        return reverse(
            url_reverse, kwargs={'id_diagnostico': diagnostico.id})


class SituacionUpdateViews(LoginRequiredMixin, UpdateView):
    model = Situacion
    form_class = SituacionForm
    template_name = 'diagnostico_emp/situacion_editar.html'
    success_url = None
    slug_field = 'id'
    slug_url_kwarg = 'id_situacion'
    messages = None
    context = {
        'form': form_class
    }

    def get_success_url(self):
        try:
            diagnostico = DiagnosticoEmpresa.objects.get(
                id=self.kwargs['id_situacion'])
            url_reverse = "mincit:planeacion"
        except DiagnosticoEmpresa.DoesNotExist:
            url_reverse = 'mincit:situacion'
        return reverse(
            url_reverse, kwargs={'id_diagnostico': diagnostico.id})


class PlaneacionViews(LoginRequiredMixin, View):
    form = PlaneacionForm
    model = Planeacion
    login_url = 'mincit:login'
    messages = None
    template = 'diagnostico_emp/planeacion.html'

    def get(self, request, *args, **kwargs):
        self.diagnostico = get_object_or_404(DiagnosticoEmpresa,
                                             id=self.kwargs['id_diagnostico'])

        if self.diagnostico.id_situacion is not None:
            return redirect('mincit:editar_planeacion',
                            self.diagnostico.id_planeacion)

        return redirect('mincit:crear_planeacion', self.diagnostico.id)


class PlaneacionCreateViews(LoginRequiredMixin, CreateView):
    model = Planeacion
    form_class = PlaneacionForm
    template_name = 'diagnostico_emp/planeacion_crear.html'
    messages = None
    context = {
        'form': form_class
    }


class PlaneacionUpdateViews(LoginRequiredMixin, UpdateView):
    model = Planeacion
    form_class = PlaneacionForm
    template_name = 'diagnostico_emp/planeacion_editar.html'
    success_url = reverse_lazy('mincit:diagnostico_emp')
    slug_field = 'id'
    slug_url_kwarg = 'id_planeacion'
    messages = None
    context = {
        'form': form_class
    }









