from django.db import models

# Create your models here.
# Modelo para representar un libro en la base de datos
# Este modelo define los campos necesarios para almacenar información sobre libros
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    def __str__(self):
        return self.titulo