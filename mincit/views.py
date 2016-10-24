from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.core.urlresolvers import reverse_lazy

from mincit.forms.forms import LoginForm, InformacionForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

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


class InicioViews(LoginRequiredMixin, View):
    login_url = 'mincit:login'

    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


@login_required(login_url='mincit:login')
def logout(request):
    logout_django(request)
    return redirect('mincit:login')


class Diagnostico_empViews(LoginRequiredMixin, View):
    login_url = 'mincit:login'

    def get(self, request,  *args, **kwargs ):
        return render(request, 'diagnostico_emp.html', {})


class InformacionViews(LoginRequiredMixin, View):
    login_url = 'mincit:login'
    success_url = reverse_lazy('client:situacion')
    template = 'informacion.html'
    form = InformacionForm(request.POST or None)
    context = {
        'form': form
    }

    def get(self, request, *args, **kwargs):
        return render(request, self.template, self.context)

    def post(self, request, *args, **kwargs):
        if self.form.is_valid():
            self.form.save()
        return HttpResponseRedirect(self.get_success_url())
