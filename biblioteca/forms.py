from django import forms
from .models import Articulo

class SearchForm(forms.Form):
	title_search = forms.CharField(max_length=100, label='Búsqueda por Título',required=False)
	author_search = forms.CharField(max_length=100, label='Búsqueda por Autor',required=False)
	keywords_search = forms.CharField(max_length=100, label='Palabras clave separadas por ;',required=False)