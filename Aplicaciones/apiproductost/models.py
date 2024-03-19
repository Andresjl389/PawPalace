from typing import Any
from django.db import models

class Temporada(models.Model):
    id = models.AutoField(primary_key=True)  # Debería ser AutoField, no "AutoField".
    nombreproducto = models.CharField(max_length=255)
    Descripcion = models.TextField()  # El nombre del campo debe ser "descripcion", en minúsculas.
    
    MES_CHOICES = [
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
    ]


    mes = models.CharField(max_length=20, choices=MES_CHOICES, null=True, verbose_name='Mes')

    class Meta:
        verbose_name_plural = 'Meses'
        
    imageproducto = models.ImageField(upload_to='temporada/', null=True)  # Debería ser "ImageField", no "FileField".

    def __str__(self):
        return self.nombreproducto



