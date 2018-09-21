from django.contrib import admin
from .models import Revista, Articulo, Autor
# Register your models here.

class RevistaInline(admin.TabularInline):
	model = Revista

class Articulo_AutoresInline(admin.TabularInline):
	model = Articulo.autores.through

class ArticuloInline(admin.TabularInline):
	model = Articulo

@admin.register(Autor)
class AdminAutor(admin.ModelAdmin):
	list_display = ('apellido', 'nombre')
	inlines = [Articulo_AutoresInline]


@admin.register(Revista)
class AdminRevista(admin.ModelAdmin):
	list_display = ('anio','mes')
	inlines = [ArticuloInline]


@admin.register(Articulo)
class AdminArticulo(admin.ModelAdmin):
	list_display = ('titulo', 'mostrar_autores', 'revista')
