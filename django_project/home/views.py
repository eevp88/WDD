from .forms import *
from .models import *
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView, ListView, CreateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext




# Create your views here.
class SaludoPresentacionTemplateView(TemplateView):
	"""docstring for SaludoPresentacion vista que  muestra la presentacion  del doctorado"""
	
	template_name='home.html'

	def get_context_data(self, **kwargs):
		context = super(SaludoPresentacionTemplateView, self).get_context_data(**kwargs)
		data = SaludoPresentacion.objects.all()
		context.update({'parrafo': data})
		return context

class HomeRedirectView(RedirectView):
    pattern_name = 'saludoPresentacion'


class ObjetivoDocTemplateView(TemplateView):
	"""docstring for ObjetivoDocTemplateView vista que  muestra los  objetivos del doctorado"""
	template_name = 'objetivo.html'

	def get_context_data(self, **kwargs):
		context= super(ObjetivoDocTemplateView, self).get_context_data(**kwargs)
		data = ObjetivoDoctorado.objects.all()

		context.update({'ObjParrafo': data})
		return context

class PerfildeGraduacionTempleView(TemplateView):
	"""docstring for PerfildeGraduacionTempleView vista que  muestra el perfil de graduacion del doctorado"""
	template_name = 'perfilGaduacion.html'

	def get_context_data(self, **kwargs):
		context= super(PerfildeGraduacionTempleView, self).get_context_data(**kwargs)
		data = PerfilGraduacion.objects.all()
		context.update({'PerfParrafo': data})
		return context

class LineaIvestigacionTemplateView(TemplateView):
	"""docstring for LineaIvestigacionTemplateView vista que  muestra el perfil de graduacion del doctorado"""
	template_name = 'lineasInvestigacion.html'

	def get_context_data(self, **kwargs):
		context= super(LineaIvestigacionTemplateView, self).get_context_data(**kwargs)
		data = LineaInvestigacion.objects.all()
		data1= TextoLineaInvestigacion.objects.all()
		context.update({'lineaInvestigacion': data, 'textoLineas': data1 })
		return context


class CursoTemplateView(TemplateView):
	"""docstring for CursoTemplateView vista que  muestra la malla curricular del doctorado, no borrar ningun ramo de esta seccion del admin"""
	template_name = 'malla.html'

	def get_context_data(self, **kwargs):
		context= super(CursoTemplateView, self).get_context_data(**kwargs)
		data1 = Curso.objects.filter(semestre = "1").order_by("indice")
		data2 = Curso.objects.filter(semestre = "2").order_by("indice")
		data3 = Curso.objects.filter(semestre = "3").order_by("indice")
		data4 = Curso.objects.filter(semestre = "4").order_by("indice")
		data5 = Curso.objects.filter(semestre = "5").order_by("indice")
		data6 = Curso.objects.filter(semestre = "6").order_by("indice")
		data7 = Curso.objects.filter(semestre = "7").order_by("indice")
		data8 = Curso.objects.filter(semestre = "8").order_by("indice")
		context.update({
			'cursoS1' : data1, 
			'cursoS2' : data2,
			'cursoS3' : data3,
			'cursoS4' : data4,
			'cursoS5' : data5,
			'cursoS6' : data6,
			'cursoS7' : data7,
			'cursoS8' : data8,

		  })
		return context

class ContactoFormView(FormView):
	"""docstring for ContactoFormView vista que  genera el formulario de contacto"""
	
	form_class = ContactForm
	template_name = 'form_contact.html'
	success_url = reverse_lazy('graciasContacto')
		

	def form_valid(self, form):
		form.send_email()
		return super(ContactoFormView, self).form_valid(form)


class ContactoGraciasTemplateView(TemplateView):
	"""docstring for LineaIvestigacionTemplateView vista que  muestra el perfil de graduacion del doctorado"""
	template_name = 'graciasContacto.html'

class ProfesoresListView(ListView):
	"""docstring for ProfesoresListView vista que  muestra una lista de los profesores del doctorado"""
	model = Profesore
	template_name = 'profesores_list.html'



class PostulacionDoctoradoFromView(FormView):
	"""docstring for PostulacionDoctorado"""
	form_class = PostulacionForm
	template_name = 'form_postulacion.html'
	success_url = reverse_lazy('postular')


	def post(self, request, *args, **kwargs):
		estado = False
		postulacion = Postulacion()
		postulacion.nombre = request.POST['nombre']
		postulacion.apellidoP = request.POST['apellidoP']
		postulacion.apellidoM = request.POST['apellidoM']
		postulacion.nacionalidad = request.POST['nacionalidad']
		postulacion.fecha_Nacimiento =request.POST['fecha_Nacimiento'] 
		postulacion.estado_civil = request.POST['estado_civil']
		postulacion.rut = request.POST['rut']
		postulacion.email =request.POST['email'] 
		postulacion.telefono = request.POST['telefono']
		postulacion.provincia_procedencia =request.POST['provincia_procedencia']
		postulacion.comuna_procedencia =request.POST['comuna_procedencia'] 
		postulacion.domiciliio_procedencia = request.POST['domiciliio_procedencia']
		postulacion.ocupacion_actual = request.POST['ocupacion_actual']
		postulacion.grado_academico = request.POST['grado_academico']
		postulacion.fecha_obtencion_grado = request.POST['fecha_obtencion_grado']
		postulacion.promedio_final_tras_examen_grado = request.POST['promedio_final_tras_examen_grado']
		postulacion.universidad_procedencia = request.POST['universidad_procedencia']
		postulacion.postulo=request.POST['postulo']	
		for x in request.FILES:
			if x == 'otros_certificados':
				postulacion.otros_certificados =request.FILES['otros_certificados']
			elif x == 'cv_academico_profecional':
				postulacion.cv_academico_profecional =request.FILES['cv_academico_profecional'] 
			elif x == 'carta_postulacion':
				postulacion.carta_postulacion = request.FILES['carta_postulacion']
			elif x =='certificados_grado_concentracion_notas_pre_postgrado':
				postulacion.certificados_grado_concentracion_notas_pre_postgrado = request.FILES['certificados_grado_concentracion_notas_pre_postgrado']
			else:
				postulacion.otros_documentos = request.FILES['otros_documentos']
		
		postulacion.full_clean()
		postulacion.save()
		estado = True
		dic = {'estado':estado}

		return render_to_response('PostulacionEnviada.html', dic, context_instance = RequestContext(request))




class ContactoRedirectView(RedirectView):
    pattern_name = 'formularioContacto'
