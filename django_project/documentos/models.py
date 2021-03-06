from django.db import models
from django.db.models import QuerySet
from django.utils.text import slugify
from home.models import Curso
from userprofile.models import UserProfile


# Create your models here.
class SlugMixin(object):

    def get_slug(self, text, model):
        slug_text = slugify(text)
        count = 2

        slug = slug_text
        while(model._default_manager.filter(slug=slug).exists()):
            slug = '{0}-{1}'.format(slug_text, count)

        return slug

class Profesor(SlugMixin, models.Model):  
    slug = models.CharField(max_length=100, blank=True)
    usuario = models.OneToOneField(UserProfile)

    def __str__(self):
        return self.usuario.user.username

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.usuario.user.username, Profesor)
        super(Profesor, self).save(*args, **kwargs)

class Carpeta(SlugMixin, models.Model):
    curso = models.ForeignKey(Curso)
    profesor =  models.ForeignKey(Profesor)
    slug = models.CharField(max_length=100, blank=True)
	
    def __str__(self):
        return "%s" % (self.curso.id)
    
    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.curso.codigo, Carpeta)
        super(Carpeta, self).save(*args, **kwargs)


class ArchivoQuerySet(QuerySet):
    def top(self):
        return self.order_by('-descarga')


class Archivo(SlugMixin, models.Model):
    titulo = models.CharField(max_length=100)
    orden = models.PositiveIntegerField(default=0)
    descarga = models.PositiveIntegerField(default=0)
    slug = models.CharField(max_length=100, blank=True)
    archivo= models.FileField(upload_to='documentos')
    profesor = models.ForeignKey(Profesor)
    curso =  models.ForeignKey(Carpeta)

    objects = ArchivoQuerySet.as_manager()

    class Meta:
        ordering = ('orden', )

    def __str__(self):
        return self.titulo


    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.titulo, Archivo)
        super(Archivo, self).save(*args, **kwargs)

