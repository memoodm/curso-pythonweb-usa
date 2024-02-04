from django.shortcuts import render

# Create your views here.
from .models import Libro


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})
