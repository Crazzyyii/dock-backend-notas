from django.contrib import admin
from .models import Nota
# Register your models here.

# Creamos una clase para personalizar cómo se ve en el admin
class NotaAdmin(admin.ModelAdmin):
    # Definimos las columnas que queremos ver en la lista
    list_display = ('title', 'created_at')
    # Agregamos una barra de búsqueda por título y contenido
    search_fields = ('title', 'content')

# Registramos el modelo Nota usando nuestra clase de configuración
admin.site.register(Nota, NotaAdmin)