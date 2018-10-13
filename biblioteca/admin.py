from django.contrib import admin
from .models import Revista, Articulo, Autor
from .views import CreacionPorLotes
from django.shortcuts import render, HttpResponse
# Register your models here.

admin.site.site_header = 'Hemeroteca admin'
admin.site.site_title = 'Hemeroteca admin'
admin.site.site_url = 'http://herokuapp.SiGeHCyT'
admin.site.index_title = 'Administración de Hemeroteca SePIDCyT'

@admin.site.register_view('creacionporlotes', 'Creación Por Lotes')
def creacionporlotes(request):
	if request.method == 'POST' and request.FILES['file']:
		myfile = request.FILES['file']
		CreacionPorLotes(myfile)
		return HttpResponse('Datos Subidos Correctamente')
	else:
		print('No se pudo subir')
	return render(request, 'admin/creacionporlotes.html')

@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
	list_display = ('apellido', 'nombre')


@admin.register(Revista)
class AdminRevista(admin.ModelAdmin):
	list_display = ('titulo', 'anio','mes')


@admin.register(Articulo)
class AdminArticulo(admin.ModelAdmin):
	list_display = ('titulo', 'mostrar_autores', 'revista')

