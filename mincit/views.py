from __future__ import print_function
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls.base import reverse
from django.views.generic import View, CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from mincit.forms import LoginForm, InformacionForm, SituacionForm, PlaneacionForm
from models import Empresa, Informacion, DiagnosticoEmpresa


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

    def get_queryset(self):
        self.empresa = get_object_or_404(Empresa, id=self.args[0])
        return DiagnosticoEmpresa.objects.filter(id_empresa=self.empresa)


class InformacionViews(LoginRequiredMixin, View):
    form = InformacionForm
    model = Informacion
    login_url = 'mincit:login'
    messages = None
    template = 'empresa/informacion.html'

    def get(self, request, *args, **kwargs):
        try:
            self.empresa = get_object_or_404(Empresa, id=self.args[0])
            self.informacion = Informacion.objects.get(id_empresa__exact=self.empresa)
            return HttpResponseRedirect('mincit:crear_informacion',
                                        self.empresa)
        except Informacion.DoesNotExist:
            return reverse_lazy('mincit:editar_informacion', self.empresa)


class InformacionCreateViews(LoginRequiredMixin, CreateView):
    model = Informacion
    form_class = InformacionForm
    template_name = 'empresa/informacion.html'
    success_url = reverse_lazy('mincit:index')
    messages = None
    context = {
        'form': form_class
    }


class InformacionUpdateViews(LoginRequiredMixin, UpdateView):
    model = Informacion
    form_class = InformacionForm
    template_name = 'empresa/informacion.html'
    success_url = reverse_lazy('mincit:index')
    messages = None
    context = {
        'form': form_class
    }


class SituacionViews(LoginRequiredMixin, View):
    form = SituacionForm
    login_url = 'mincit:login'
    success_url = reverse_lazy('planeacion')
    template = 'diagnostico_emp/situacion.html'
    context = {
        'form': form
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs ):
        self.form = SituacionForm(request.POST)

        return render(request, 'diagnostico_emp/planeacion.html', self.context)


class PlaneacionViews(LoginRequiredMixin, View):
    form = PlaneacionForm
    login_url = 'mincit:login'
    success_url = reverse_lazy('organizacion')
    template = 'diagnostico_emp/planeacion.html'
    context = {
        'form': form
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs ):
        self.form = PlaneacionForm(request.POST)
        if self.form.is_valid():
            self.form.save()
            return render(request, 'diagnostico_emp/planeacion.html', self.context)

        return render(request, 'diagnostico_emp/organizacion.html', self.context)















