from django.shortcuts import render, redirect
from Aplicaciones.recetas.models import Receta
from .forms import AdminForm

# Create your views here.

def vista_recetas(request):
    if request.method == 'GET':
        lista = Receta.objects.all()
        return render(request, 'adm_recetas.html',{'recetas':lista})
    else:
        if request.POST['buscar'] == '':
            lista = Receta.objects.all()
            return render(request, 'adm_recetas.html',{'recetas':lista})
        else:
            lista = Receta.objects.filter(Ingrediente_principal__icontains=request.POST['buscar'])
            return render(request, 'adm_recetas.html',{'recetas':lista})



def crear_receta(request):
    crear_r = AdminForm(request.POST or None, request.FILES or None)
    if crear_r.is_valid():
        crear_r.save()
        return redirect('adm_recetas')
    return render(request, 'crear_receta.html',{'creado': crear_r})



def eliminar_receta(request, id):
    eliminar = Receta.objects.get(id=id).delete()
    return redirect('adm_recetas')


def editar_receta(request, id):
    Editado = Receta.objects.get(id=id)
    editar_r = AdminForm(request.POST or None, request.FILES or None, instance=Editado)
    if editar_r.is_valid() and request.POST:
        editar_r.save()
        return redirect('adm_recetas')
    return render(request, 'editar_receta.html',{'creado': editar_r})