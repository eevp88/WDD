from django.contrib import admin

# Register your models here.
from .models import *

class CursoAdmin(admin.ModelAdmin):
	list_display = ('id', 'codigo','creditos', 'nombre', 'indice', 'semestre', 'tipo')
	list_filter = ( 'semestre','tipo')
	search_fields = ('nombre','tipo',)
		
admin.site.register(SaludoPresentacion)
admin.site.register(ObjetivoDoctorado)
admin.site.register(PerfilGraduacion)
admin.site.register(LineaInvestigacion)
admin.site.register(TextoLineaInvestigacion)
admin.site.register(Profesore)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Postulacion)
