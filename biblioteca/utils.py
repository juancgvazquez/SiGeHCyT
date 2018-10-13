import pandas as pd
from .models import Revista, Articulo, Autor
from django.db import transaction

@transaction.atomic()
def CreacionPorLotes(file):
	df = pd.read_excel(file)
	#Creo Articulos, autores, revistas
	for index,row in df.iterrows():
		if not Revista.objects.filter(titulo=row['Título_revista'], anio=row['Año'], mes=row['Mes']).exists():
			Rev = Revista.objects.create(titulo=row['Título_revista'], anio=row['Año'], mes=row['Mes'])
		else:
			Rev = Revista.objects.get(titulo=row['Título_revista'], anio=row['Año'], mes=row['Mes'])
		autores = row['Autores'].split('; ')
		autoresobj = []
		for aut in autores:
				if type(aut) == list:
					for ape, nom in aut.split(','):
						if not Autor.objects.filter(apellido=ape, nombre=nom).exists():
							autor = Autor.objects.create(apellido=ape, nombre=nom)
						else:
							autor = Autor.objects.get(apellido=ape, nombre=nom)
				else:
					if not Autor.objects.filter(apellido=aut).exists():
						autor = Autor.objects.create(apellido=aut)
					else:
						autor = Autor.objects.get(apellido=aut)
				autoresobj.append(autor)
		articulo = Articulo.objects.create(titulo=row['Título'], revista=Rev,numero=row['Nro'],pagina=row['Pág.'],
								resumen=row['Resumen'])
		articulo.autores.set(autoresobj)


