from django.shortcuts import render



def inicio(request):
    titulo = "titulo dinámico"
    return render(request, "pages/inicio.html",{'titulo': 'Inicio'})

def suscripcion(request):
    titulo = "titulo dinámico"
    return render(request, "pages/suscripcion.html",{'titulo':'Detalle de la suscripcion'})

def principal(request):
    return render(request, "pages/principal.html",{})




    
def padmin(request):
    return render(request, "pages/p_administrativo.html", {'titulo': 'Perfil Administrativo'})