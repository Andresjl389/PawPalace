from django.db import models
from db_conection import db


# Create your models here.

class CustomUser(models.Model):
    # Definimos los campos que deseamos para el modelo de usuario
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    # Agrega más campos personalizados según tus necesidades

    class Meta:
        db_table = 'custom_user'  # Define el nombre de la colección en MongoDB

    def __str__(self):
        return self.username