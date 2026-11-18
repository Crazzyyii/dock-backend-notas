from django.db import models

# Create your models here.
class Nota(models.Model):
    # CharField para textos cortos. Representa un VARCHAR en SQL.
    title = models.CharField(max_length=200, verbose_name="Título")
    
    # TextField para textos largos sin límite. Representa un TEXT en SQL.
    content = models.TextField(verbose_name="Contenido")
    
    # auto_now_add registra automáticamente la fecha y hora de creación.
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    # Método "dunder string" para que se vea bien el nombre en el Admin de Django
    def __str__(self):
        return self.title