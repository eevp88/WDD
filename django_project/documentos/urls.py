from django.conf.urls import patterns, url

from .views import *

urlpatterns = patterns('',
   # url(r'^login/$', LoginView.as_view(), name='login'),
    #url(r'^profile/$', ProfileView.as_view(), name='profile'),
    #url(r'^perfil/$', PerfilRedirectView.as_view(), name='perfil'),
    #url(r'^logout/$', LogoutView.as_view(), name='log-out'),}
    url(r'^carpetas/$', CarpetaListView.as_view(), name='carpetas_list'),
    url(r'^carpetas/(?P<pk>[\w\-]+)/$', CarpetaDetailView.as_view(), name='carpeta_detail'),
)