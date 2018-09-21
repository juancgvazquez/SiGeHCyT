from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .utils import CreacionPorLotes
from .models import Revista, Autor, Articulo

# Create your views here.
@login_required
def upload_file(request):
	if request.method == 'POST' and request.FILES['file']:
		myfile = request.FILES['file']
		CreacionPorLotes(myfile)
		return HttpResponse('Datos Subidos Correctamente')
	else:
		print('No se pudo subir')
	return render(request,'biblioteca/creacion_por_lote.html')


def index(request):
	"""
	Home, página principal
	"""
	#Generamos estadísticas
	num_articulos = Articulo.objects.count()
	num_revistas = Revista.objects.count()
	num_autores = Autor.objects.count()

	return render(
		request,
		'index.html',
		context={'num_articulos':num_articulos, 'num_revistas':num_revistas, 'num_autores':num_autores}

	)


class ListaArticulos(generic.ListView):
	model = Articulo
	paginate_by = 25


class ListaAutores(generic.ListView):
	model = Autor
	paginate_by = 25


class ListaRevistas(generic.ListView):
	model = Revista
	paginate_by = 25


class DetalleArticulo(generic.DetailView):
	model = Articulo


class DetalleAutor(generic.DetailView):
	model = Autor


class DetalleRevista(generic.DetailView):
	model = Revista
