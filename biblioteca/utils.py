import pandas as pd
from .models import Revista, Articulo, Autor
from django.db import transaction

@transaction.atomic()
def CreacionPorLotes(file):
	df = pd.read_excel(file, sheet_name='Contenidos')
	#Creo Articulos, autores, revistas
	for index,row in df.iterrows():
		if not Revista.objects.filter(anio=row['Año'], mes=row['Mes']).exists():
			Rev = Revista.objects.create(anio=row['Año'], mes=row['Mes'])
		else:
			Rev = Revista.objects.get(anio=row['Año'], mes=row['Mes'])
		autores = row['Autores'].replace(' y ', ', ').split(', ')
		autoresobj = []
		for y in autores:
			if not Autor.objects.filter(apellido=y).exists():
				autor = Autor.objects.create(apellido=y)
			else:
				autor = Autor.objects.get(apellido=y)
			autoresobj.append(autor)
		articulo = Articulo.objects.create(titulo=row['Título'], revista=Rev,numero=row['Nro'],pagina=row['Pág.'],
								resumen=row['Resumen'])
		articulo.autores.set(autoresobj)


