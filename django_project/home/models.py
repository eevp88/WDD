#encoding:utf-8
from django.db import models
from django.utils.encoding import smart_unicode

# Create your models here.
class SaludoPresentacion (models.Model):
	parrafo = models.TextField()
	class Meta:
		ordering=["id"]
		verbose_name_plural= "Saludo Presentación"

	def __unicode__(self):
		return smart_unicode(self.parrafo)

class ObjetivoDoctorado(models.Model):
	ObjParrafo= models.TextField()
	class Meta:
		ordering=["id"]
		verbose_name_plural="Objetivo del Doctorado"
	def __unicode__(self):
		return smart_unicode(self.ObjParrafo)
		
class PerfilGraduacion(models.Model):
	PerfParrafo = models.TextField()
	class Meta:
		ordering= ["id"]
		verbose_name_plural ="Perfil de Graduación"
	def __unicode__(self):
		return smart_unicode(self.PerfParrafo)

class LineaInvestigacion(models.Model):
	LineaInvestigativa = models.CharField(max_length=100)
	class Meta:
		ordering=["id"]
		verbose_name_plural= "Línea de Investigación"
	
	def __unicode__(self):
		return smart_unicode(self.LineaInvestigativa)

class TextoLineaInvestigacion(models.Model):
	TextoLineaInvestigativa = models.TextField()
	class Meta:
		ordering=["id"]
		verbose_name_plural= "Textos de Línea Investigación"
	def __unicode__(self):
		return smart_unicode(self.TextoLineaInvestigativa)

class Profesore(models.Model):
	fotoAvatar= models.ImageField(upload_to='fotoAvatars')
	nombre = models.CharField(max_length=150)
	cvlink = models.CharField(max_length=200)

	def __unicode__(self):
		return smart_unicode(self.nombre)


tipo_curso = (
	('Asignatura Obligatoria','Asignatura Obligatoria'),
        ('Asignatura Optativa','Asignatura Optativa'),
	('Asignatura Obligatoria Principal','Asignatura Obligatoria Principal'),
	('Asignatura Obligatoria Seminario','Asignatura Obligatoria Seminario'),
	('Asignatura Optativa Principal','Asignatura Optativa Principal'),
	('Asignatura Optativa Seminario','Asignatura Optativa Seminario'),
	)
N_semestre = (
	('1','I'),
	('2','II'),
	('3','III'),
	('4','IV'),
	('5','V'),
	('6','VI'),
	('7','VII'),
	('8','VIII'),
	)

Nramo = (
	('1','1'),
	('2','2'),
	('3','3'),
	('4','4'),
	('5','5'),
	('6','6'),
	('7','7'),
	)

class Curso(models.Model):
	codigo = models.CharField(max_length=10)
	creditos = models.IntegerField()
	indice = models.CharField(max_length= 2, choices = Nramo)
	nombre = models.CharField(max_length=100)
	semestre = models.CharField(max_length=8, choices = N_semestre )
	tipo = models.CharField(max_length= 32, choices=tipo_curso)

	def __unicode__(self):
		return smart_unicode(self.nombre)

class Postulacion(models.Model):
	nombre = models.CharField(max_length=200)
	apellidoP =models.CharField(max_length=200)
	apellidoM = models.CharField(max_length=200)
	nacionalidad = models.CharField(max_length =200)
	fecha_Nacimiento = models.DateField(null=True, blank=True)
	estado_civil = models.CharField(max_length= 200)
	rut = models.CharField(max_length= 20)
	email = models.EmailField(max_length = 200)
	telefono = models.CharField(max_length= 30)
	provincia_procedencia = models.CharField(max_length=200)
	comuna_procedencia = models.CharField(max_length=200)
	domiciliio_procedencia = models.CharField(max_length=200)
	ocupacion_actual = models.CharField(max_length=200)
	grado_academico = models.CharField (max_length=200)
	fecha_obtencion_grado = models.DateField(null=True, blank=True)
	promedio_final_tras_examen_grado = models.CharField(max_length=200)
	universidad_procedencia= models.CharField(max_length=200)
	postulo = models.CharField(max_length=200)
	cv_academico_profecional = models.FileField(upload_to='docPostulacion/CV', max_length=200)
	carta_postulacion = models.FileField(upload_to='docPostulacion/cartaPostulacion', max_length=200)
	certificados_grado_concentracion_notas_pre_postgrado = models.FileField(max_length=200,upload_to='docPostulacion/certificados')
	otros_certificados = models.FileField(max_length=200, upload_to='docPostulacion/otrosCertificados', null=True, blank=True)
	otros_documentos = models.FileField(max_length=200, upload_to='docPostulacion/otrosDocumentos',  null=True, blank=True)

	def __unicode__(self):
		return smart_unicode(self.nombre)


from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
 
from django.contrib.sessions.models import Session
 
@receiver(post_save)
def clear_cache(sender, **kwargs):
    if sender != Session:
        cache.clear()
