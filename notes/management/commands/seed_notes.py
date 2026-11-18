from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from notes.models import Nota

class Command(BaseCommand):
    help = 'Puebla la base de datos con notas de prueba y crea el superusuario'

    def handle(self, *args, **kwargs):
        # 1. Crear el superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@correo.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Superusuario "admin" creado con contraseña "admin123"'))
        else:
            self.stdout.write(self.style.NOTICE('El usuario "admin" ya existe.'))

        # 2. Limpiamos notas previas para no duplicar
        Nota.objects.all().delete()
        self.stdout.write(self.style.WARNING('Viejas notas eliminadas.'))

        # 3. Datos simulados
        notas_mock = [
            {"title": "Primera Clase", "content": "Aprendimos sobre entornos virtuales con el profesor Helton."},
            {"title": "DockerCompose", "content": "Levanta servicios simultáneos con facilidad."},
            {"title": "Render y Nube", "content": "La plataforma PAAS para subir nuestros proyectos backend."}
        ]

        for item in notas_mock:
            Nota.objects.create(title=item['title'], content=item['content'])

        self.stdout.write(self.style.SUCCESS('¡Semilla de notas plantada exitosamente!'))
