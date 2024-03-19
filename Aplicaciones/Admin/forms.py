from django import forms
from Aplicaciones.recetas.models import Receta

class AdminForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'