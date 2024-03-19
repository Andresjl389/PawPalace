from django.shortcuts import render
from .models import Pqrs
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def info(request):
    titulo = "titulo dinámico"
    
    if request.method == "GET":
        return render(request, "infop.html",{'titulo':'PQRS'})
    else:
        c_name = request.POST["name"]
        c_email = request.POST["email"]
        c_phone = request.POST["phone"]
        c_message = request.POST["message"]
        objects_contacto = Pqrs(name=c_name, email=c_email, phone=c_phone, message=c_message)
        objects_contacto.save()
        send_email(objects_contacto)
        respuesta(objects_contacto)
        
        print(c_name, c_email, c_phone, c_message)
        
        return render(request, "infop.html",{'titulo':'PQRS'})
    
    
def send_email(send_email):
    subjects = f'LocalFood responder preguntas a {send_email.name}'
    message = f"nombre: {send_email.name},\n email: {send_email.email},\n telefono: {send_email.phone}, \n mensaje: {send_email.message}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ["local.food.a4@gmail.com"]
    send_mail(subjects, message, email_from, recipient_list)
    return True
    

def respuesta(respuesta):
    subject = "Hola, gracias por contactarse con LocalFood"
    message = f"señor@ {respuesta.name} estamos trabajando para darle respuesta a sus preguntas"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [f"{respuesta.email}"]
    send_mail( subject, message, email_from, recipient_list )
    return True


def PQRS(request):
    
    if request.method == "GET":
        obj_quejas = Pqrs.objects.all()
        return render(request, 'PQRS.html',{'q':obj_quejas})
    else:
        if request.POST['buscar'] == "":
            obj_quejas = Pqrs.objects.all()
            return render(request, 'PQRS.html',{'q':obj_quejas})
        else:
            nombre = request.POST['buscar']
            obj_quejas = Pqrs.objects.filter(name__icontains = nombre)
            return render(request, 'PQRS.html', {'q':obj_quejas, 'encontrados':'Elementos encontrados'})