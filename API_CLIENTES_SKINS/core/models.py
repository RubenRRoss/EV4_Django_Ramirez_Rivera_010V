from django.db import models

# Create your models here.


class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria


class Cliente(models.Model):
    rut = models.CharField(max_length=6, primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    correo = models.CharField(max_length=40, verbose_name='Correo')
    telefono = models.IntegerField(verbose_name='Telefono')
    direccion = models.CharField(max_length=50, verbose_name='Direccion')

    def __str__(self):
        return self.nombre

