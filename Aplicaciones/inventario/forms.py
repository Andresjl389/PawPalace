from django import forms
from .models import inventario 

class LibroForm(forms.ModelForm):
    class Meta:
        model = inventario
        fields = '__all__'