from django import forms
from .models import Libro

# Formulario para crear y editar libros
# Este formulario se basa en el modelo Libro y permite ingresar los datos necesarios
class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'descripcion', 'fecha_publicacion', 'isbn']