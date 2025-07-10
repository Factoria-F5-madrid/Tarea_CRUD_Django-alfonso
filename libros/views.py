from django.shortcuts import render, get_object_or_404, redirect

# Importamos las vistas necesarias de Django
from .models import Libro
from .forms import LibroForm


# Create your views here.

# Vistas para manejar las operaciones CRUD de los libros
# Estas vistas permiten listar, crear, editar y eliminar libros en la aplicación
# las vistas están diseñadas para interactuar con el modelo Libro y los formularios correspondientes
def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista_libros.html', {'libros': libros})

# Vistas para mostrar los detalles de un libro
# Esta vista muestra los detalles de un libro específico
def detalle_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'libros/detalle_libro.html', {'libro': libro})

# Vistas para crear un libro
# Esta vista maneja la creación de un nuevo libro
def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_libros')
    else:
        form = LibroForm()
    return render(request, 'libros/crear_libro.html', {'form': form})

# Vistas para editar un libro
# Esta vista maneja la edición de un libro específico
def editar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('detalle_libro', libro_id=libro.id)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar_libro.html', {'form': form, 'libro': libro})

# Vistas para eliminar un libro
# Esta vista maneja la eliminación de un libro específico
def eliminar_libro(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        return redirect('lista_libros')
    return render(request, 'libros/eliminar_libro.html', {'libro': libro})