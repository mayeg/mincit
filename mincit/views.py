from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.urls.base import reverse
from django.views.generic import View, DetailView
from django.views.generic.list import ListView
from mincit.forms import LoginForm, InformacionForm, SituacionForm, PlaneacionForm
from models import Empresa, Informacion, Diagnostico_Emp


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


class Diagnostico_empViews(LoginRequiredMixin, ListView, DetailView):
    login_url = 'mincit:login'
    model = Diagnostico_Emp
    template_name = 'diagnostico_emp/diagnostico_emp.html'
    paginate_by = 10
    slug_field = 'id_empresa'

    def get_context_data(self, **kwargs):
        context = super(Diagnostico_empViews, self).get_context_data(
            **kwargs)
        return context

    def get_queryset(self):
        id_empresa = self.kwargs['id_empresa']
        modelo = Diagnostico_Emp.objects.get(id_empresa=id_empresa)

    def get(self, request, *args, **kwargs):
        return render(request, 'diagnostico_emp/diagnostico_emp.html', {})


class InformacionViews(LoginRequiredMixin, View):
    form = InformacionForm
    model = None
    login_url = 'mincit:login'
    success_url = reverse_lazy('situacion')
    template = 'diagnostico_emp/informacion.html'
    messages = None
    context = {
        'form': form
    }


    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs ):
        self.form = InformacionForm(request.POST)

        if self.form.is_valid():
            self.form.save()
            return render(request, 'diagnostico_emp/situacion.html',
                          self.context)

        return render(request, self.template, self.context)


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















