from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from documentos.models import *
from userprofile.mixins import LoginRequiredMixin
# Create your views here.


class JsonResponseMixin(object):

    def response_handler(self):
        format = self.request.GET.get('format', None)
        if format == 'json':
            return self.json_to_response()

        context = self.get_context_data()
        return self.render_to_response(context)

    def json_to_response(self):
        data = self.get_data()
        return JsonResponse(data, safe=False)

class CarpetaListView(LoginRequiredMixin, JsonResponseMixin, ListView):
    model = Carpeta
    template_name = 'carpeta_list.html'
    

    #def get(self, request, *args, **kwargs):
    #    self.object_list = self.get_queryset()
    #    return self.response_handler()

    #def get_context_data(self, **kwargs):
    #    context = super(CarpetaListView, self).get_context_data(**kwargs)
    #    page = self.request.GET.get('page')

    #    context.update({'page': page})
    #    return context

    #def get_data(self):
    #    data = [{
    #        'nombre_curso': curso.nombre,
    #        'semestre': folder.carpeta.curso.semestre,
    #        'profesor': folder.carpeta.profesor.usuario.user.username,
    #    } for folder in self.object_list]

    #    return data

    def get_queryset(self):
        if self.kwargs.get('profesor'):
            queryset = self.model.objects.filter(profesor__slug__contains=self.kwargs['profesor'])
        else:
            queryset = super(CarpetaListView, self).get_queryset()

        return queryset

class CarpetaDetailView(LoginRequiredMixin, JsonResponseMixin, DetailView):
    model = Carpeta
    template_name = 'carpeta_detail.html'
    # slug_url_kwarg = 'djangoavanzado'
    # slug_field = 'title'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.response_handler()

    def get_data(self):
        data = {
            'carpeta':{
                'titulo': self.object.curso,
                'profesor': self.object.profesor.usuario,
                'documentos': [t.titulo for t in self.object.archivo_set.all()]
            }
        }

        return data
