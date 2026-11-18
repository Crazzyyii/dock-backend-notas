from django.shortcuts import render

# Create your views here.

from .models import Nota

def index(request):
    # Obtenemos las notas de la base de datos PostgreSQL, las mas recientes primero
    notas = Nota.objects.all().order_by('-created_at')
    return render(request, 'notes/index.html', {'notas': notas})
