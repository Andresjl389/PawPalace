from typing import Any
from django.db import models

# Create your models here.
class inventario(models.Model):

    id= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=100, verbose_name='Titulo')
    imagen= models.ImageField(upload_to='proyectos/' ,verbose_name='Imagen', null=True)
    descripcion= models.IntegerField(null=True, verbose_name='Cantidad')

    objects = models.Manager()

    def __str__(self):
        fila= "Titulo:" + self.titulo +  " - " + "Descripcion:" + str(self.descripcion)
        return fila
    
    def delete(self, using= None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

