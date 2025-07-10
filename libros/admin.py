
# sistema_libros/libros/admin.py
# Este archivo se encarga de registrar los modelos en el panel de administración de Django
from django.contrib import admin

# Importamos el modelo Libro para poder registrarlo en el admin
from .models import Libro

# Register your models here.
# Aquí registramos el modelo Libro en el panel de administración de Django
# Esto permite que podamos gestionar los libros desde la interfaz de administración
@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'fecha_publicacion', 'isbn')
    search_fields = ('titulo', 'autor', 'isbn')
    list_filter = ('fecha_publicacion',)
