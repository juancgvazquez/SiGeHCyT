from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from .utils import CreacionPorLotes
from .forms import SearchForm
from .models import Revista, Autor, Articulo


def search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title_search']
			author = form.cleaned_data['author_search']
			keywords = form.cleaned_data['keywords_search']
			result = Articulo.objects.all()
			if title != '':
				result = result.filter(titulo__contains=title)
			if author != '':
				if result:
					result = result.filter(autores__apellido__contains=author)
				else:
					result = Articulo.objects.filter(autores__apellido__contains=author)
			if keywords != '':
				keywords = keywords.split(';')
				if result:
					for x in keywords:
						result = result.filter(resumen__contains=str(x))
				else:
					for x in keywords:
						result = Articulo.objects.filter(resumen__contains=str(x))
		return render(request, 'biblioteca/busqueda.html', {'form':form, 'searchResults': result})
	else:
		form = SearchForm()

	return render(request, 'biblioteca/busqueda.html', {'form':form,})

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
	paginate_by = 50


class ListaAutores(generic.ListView):
	model = Autor
	paginate_by = 50


class ListaRevistas(generic.ListView):
	model = Revista
	paginate_by = 50


class DetalleArticulo(generic.DetailView):
	model = Articulo


class DetalleAutor(generic.DetailView):
	model = Autor


class DetalleRevista(generic.DetailView):
	model = Revista
