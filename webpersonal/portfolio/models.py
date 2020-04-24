from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='projects')
    link = models.URLField(verbose_name='Dirección web', null=True, blank=True)
    # Los campos created y updated son de solo lectura y no se muetran por defecto en el panelde administrador,
    # pero se puede hacer una configuración extendida en admin.py para mostrarlos
    created = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación') # Se ejecuta al crearse una instancia
    updated = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de modificación') # Se ejecuta cada vez que se actualiza una instancia

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created'] # Ordena los post en orden decreciente

    # Cambia el nombre Project object (1) al título real
    def __str__(self):
        return self.title
