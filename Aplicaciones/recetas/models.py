from django.db import models
from db_conection import db

# Create your models here.


class Receta(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre_receta = models.CharField(max_length=255)
    Descripcion = models.TextField()
    Ingredientes = models.TextField()
    Ingrediente_principal = models.CharField(max_length=255)
    imageproj = models.FileField(upload_to = 'proyectos/', null=True,)
    
    def __str__(self):
        return self.Nombre_receta