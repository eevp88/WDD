from django.contrib import admin
from .models import Profesor, Carpeta, Archivo
# Register your models here.

class ArchivoAdmin(admin.ModelAdmin):
	list_display = ('id','titulo', 'slug', 'archivo','profesor', 'curso')

admin.site.register(Profesor)
admin.site.register(Carpeta)
admin.site.register(Archivo, ArchivoAdmin)
