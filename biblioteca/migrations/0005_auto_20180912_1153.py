# Generated by Django 2.1.1 on 2018-09-12 11:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20180912_0105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ejemplar',
            old_name='Revista',
            new_name='revista',
        ),
        migrations.AlterField(
            model_name='ejemplar',
            name='id',
            field=models.UUIDField(default=uuid.UUID('cb7a0d05-1054-4722-8d70-a174a401b131'), help_text='Identificación única del Ejemplar', primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='anio',
            field=models.IntegerField(help_text='Ingresar Año de la Revista', verbose_name='Año'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='mes',
            field=models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')], help_text='Ingresar mes de la Revista', verbose_name='Mes'),
        ),
    ]
