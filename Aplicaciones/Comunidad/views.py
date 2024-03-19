from django.shortcuts import render, redirect
from .models import Comentarios,Respuesta



def comentar(request):
    
    if request.method == 'POST':
        
        print(request.POST['comentario'])
        comentario = request.POST['comentario']
        obj_comment = Comentarios(text=comentario)
        obj_comment.save()
        
        return redirect('comenComunidad')
    
    else:
        mis_comentarios = Comentarios.objects.all()
        return render(request, 'create_thread.html',{'c':mis_comentarios})

def rta(request):
    if request.method == 'POST':
        print(request.POST['custID'])
        print(request.POST['Resp'])
        
        textRespuesta = request.POST['Resp']
        custid = request.POST['custID']
        obj_res = Respuesta(textRes=textRespuesta, commentID=custid)
        obj_res.save()
        
        return redirect('comenComunidad')    
        
    else:
        mis_resp = Respuesta.objects.all()
        return render(request, 'create_thread.html',{'r':mis_resp})