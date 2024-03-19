from django.db import models
from django.contrib.auth.models import User

class Comentarios(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField(max_length=2000)

    class Meta:
        db_table = 'Comentarios'

class Respuesta(models.Model):
    id = models.AutoField(primary_key=True)
    textRes = models.CharField(max_length=2000)
    commentID = models.IntegerField()
    
    class Meta:
        db_table = 'Respuesta'
    

