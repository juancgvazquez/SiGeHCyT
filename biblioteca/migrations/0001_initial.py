# Generated by Django 2.1.2 on 2018-10-13 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Título del Artículo', max_length=100)),
                ('numero', models.IntegerField(help_text='Número de Artículo en la Revista')),
                ('pagina', models.IntegerField(help_text='Página del Artículo')),
                ('resumen', models.TextField(help_text='Resumen del Artículo')),
            ],
            options={
                'verbose_name': 'Artículo',
                'verbose_name_plural': 'Artículos',
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, help_text='Nombre del Autor', max_length=100, null=True)),
                ('apellido', models.CharField(help_text='Apellido del Autor', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Autores',
                'ordering': ['apellido', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(help_text='Ingresar el título Revista', max_length=100, verbose_name='Título')),
                ('mes', models.CharField(choices=[('Ene', 'Enero'), ('Feb', 'Febrero'), ('Mar', 'Marzo'), ('Abr', 'Abril'), ('May', 'Mayo'), ('Jun', 'Junio'), ('Jul', 'Julio'), ('Ago', 'Agosto'), ('Sep', 'Septiembre'), ('Oct', 'Octubre'), ('Nov', 'Noviembre'), ('Dic', 'Diciembre')], help_text='Ingresar mes de la Revista', max_length=3, verbose_name='Mes')),
                ('anio', models.IntegerField(verbose_name='Año')),
            ],
        ),
        migrations.AddField(
            model_name='articulo',
            name='autores',
            field=models.ManyToManyField(to='biblioteca.Autor'),
        ),
        migrations.AddField(
            model_name='articulo',
            name='revista',
            field=models.ForeignKey(help_text='Revista en la que está el artículo', null=True, on_delete=django.db.models.deletion.SET_NULL, to='biblioteca.Revista'),
        ),
    ]
