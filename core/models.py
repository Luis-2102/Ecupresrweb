from django.db import models

# Create your models here.

class Icono(models.Model):
    img= models.ImageField(verbose_name="Iconos", upload_to="iconos/")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")
    class Meta:
        verbose_name = "Icono"
        verbose_name_plural = "Iconos"
        ordering = ["-created"]
    def __str__(self):
        return f"Icono creado el {self.created.strftime('%Y-%m-%d')}"
    
