from django.conf.urls import patterns, url

from .views import LoginView, ProfileView, PerfilRedirectView, LogoutView, PrincipalTemplateView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^principal/$', PrincipalTemplateView.as_view(), name='principal'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
    url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
    url(r'^logout/$', LogoutView.as_view(), name='log-out'),
)
