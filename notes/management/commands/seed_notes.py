import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from notes.models import Nota

class Command(BaseCommand):
    help = 'Puebla la base de datos con notas de prueba y crea el superusuario seguro'

    def handle(self, *args, **kwargs):
        # 1. Leer credenciales del admin desde Variables de Entorno
        admin_user = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
        admin_email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@correo.com')
        admin_password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

        # 2. Crear el superusuario solo si se definió una contraseña y aún no existe
        if admin_password and not User.objects.filter(username=admin_user).exists():
            User.objects.create_superuser(admin_user, admin_email, admin_password)
            self.stdout.write(self.style.SUCCESS(f'Superusuario "{admin_user}" creado exitosamente.'))
        elif not admin_password:
            self.stdout.write(self.style.WARNING('No se definió DJANGO_SUPERUSER_PASSWORD en las variables de entorno.'))
        else:
            self.stdout.write(self.style.NOTICE(f'El usuario "{admin_user}" ya existe.'))

        # 3. Limpiamos notas previas para no duplicar
        Nota.objects.all().delete()
        self.stdout.write(self.style.WARNING('Viejas notas eliminadas.'))

        # 4. Datos simulados
        notas_mock = [
            {"title": "Primera Clase", "content": "Aprendimos sobre entornos virtuales con el profesor Helton."},
            {"title": "DockerCompose", "content": "Levanta servicios simultáneos con facilidad."},
            {"title": "Render y Nube", "content": "La plataforma PAAS para subir nuestros proyectos backend."}
        ]

        for item in notas_mock:
            Nota.objects.create(title=item['title'], content=item['content'])

        self.stdout.write(self.style.SUCCESS('¡Semilla de notas plantada exitosamente!'))
