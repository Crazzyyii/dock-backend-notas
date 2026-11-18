from django.contrib import admin
from .models import Nota

# Títulos personalizados para el panel de administración
admin.site.site_header = "⚡ CloudNotes • BackEnd"
admin.site.site_title = "CloudNotes Admin"
admin.site.index_title = "Panel de Gestión PostgreSQL"

class NotaAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at',)

admin.site.register(Nota, NotaAdmin)
