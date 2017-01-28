from django.conf.urls import patterns, url
from views import *


urlpatterns = patterns('',
    url(r'^home/$', SaludoPresentacionTemplateView.as_view(), name='saludoPresentacion'),
    url(r'^$', HomeRedirectView.as_view(), name='home'),
    url(r'^objetivos/$', ObjetivoDocTemplateView.as_view(), name='objetivoDoc'),
    url(r'^perfil/$', PerfildeGraduacionTempleView.as_view(), name='perfilGraduacion'),
   	url(r'^linea/$', LineaIvestigacionTemplateView.as_view(), name='lineaInvestigacion'),
   	url(r'^contacto/$', ContactoFormView.as_view(), name='formularioContacto'),
   	url(r'^graciasContacto/$', ContactoGraciasTemplateView.as_view(), name='graciasContacto'),
    url(r'^profesores/$', ProfesoresListView.as_view(), name='profesores_list'),
    url(r'^malla/$', CursoTemplateView.as_view(), name='malla'),
    url(r'^postulacion/$', PostulacionDoctoradoFromView.as_view(), name='postular'),

    #url(r'^albums/(?P<artist>[\w\-]+)/$', AlbumListView.as_view(), name='album_list'),
    #url(r'^albums/detail/(?P<slug>[\w\-]+)/$', AlbumDetailView.as_view(), name='album_detail'),
    #url(r'^tracks/top/$', TopTrackListView.as_view(), name='top_tracks'),
)
