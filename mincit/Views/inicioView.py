from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth import logout as logout_django
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from mincit.Forms.forms import LoginForm
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin

class InicioViews(LoginRequiredMixin, View):
    login_url= 'mincit:login'

    def get(self, request, *args, **kwargs):
        return render(request, 'inicio.html', {})


