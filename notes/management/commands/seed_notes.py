# Archivo: notes/management/commands/seed_notes.py
from django.core.management.base import BaseCommand
from notes.models import Nota

class Command(BaseCommand):
    # El mensaje de ayuda al ejecutar: python manage.py help seed_notes
    help = 'Puebla la base de datos con notas de prueba'

    def handle(self, *args, **kwargs):
        # Limpiamos notas previas para no duplicar al ejecutar el comando muchas veces
        Nota.objects.all().delete()
        self.stdout.write(self.style.WARNING('Viejas notas eliminadas.'))

        # Datos simulados
        notas_mock = [
            {"title": "Primera Clase", "content": "Aprendimos sobre entornos virtuales con el profesor Helton."},
            {"title": "DockerCompose", "content": "Levanta servicios simultáneos con facilidad."},
            {"title": "Render y Nube", "content": "La plataforma PAAS para subir nuestros proyectos backend."}
        ]

        for item in notas_mock:
            # El método create hace el INSERT en SQL directamente
            Nota.objects.create(title=item['title'], content=item['content'])

        # Mensaje de éxito en terminal de color verde
        self.stdout.write(self.style.SUCCESS('¡Semilla de notas plantada exitosamente!'))