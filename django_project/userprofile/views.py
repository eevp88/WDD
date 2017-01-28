from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, RedirectView, FormView
from userprofile.mixins import LoginRequiredMixin


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy('principal')
    
    def form_valid(self, form):
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)

        login(self.request, form.user_cache)
        
        return super(LoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context

class LogoutView(RedirectView):
    pattern_name = 'saludoPresentacion'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)

        if self.request.user.is_authenticated():
            context.update({'userprofile': self.get_userprofile()})

        return context

    def get_userprofile(self):
        return self.request.user.userprofile


class PerfilRedirectView(RedirectView):
    pattern_name = 'profile'


class PrincipalTemplateView(LoginRequiredMixin, TemplateView):
    """docstring for PrincipalTemplateView vista que  muestra el el panel principal una vez logeado el usuario"""
    template_name = 'principal.html'


