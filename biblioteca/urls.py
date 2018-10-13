from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^articulos/$', views.ListaArticulos.as_view(), name='Artículos'),
	url(r'^articulos/(?P<pk>\d+)$', views.DetalleArticulo.as_view(), name='DetalleArtículos'),
	url(r'^autores/$', views.ListaAutores.as_view(), name='Autores'),
	url(r'^autores/(?P<pk>\d+)$', views.DetalleAutor.as_view(), name='DetalleAutores'),
	url(r'^revistas/$', views.ListaRevistas.as_view(), name='Revistas'),
	url(r'^revistas/(?P<pk>\d+)$', views.DetalleRevista.as_view(), name='DetalleRevistas'),
	url(r'^buscar/$', views.search, name='Búsqueda'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)