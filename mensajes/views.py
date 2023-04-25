from django.shortcuts import render, redirect
from .models import Mensaje
from django.contrib.auth.models import User
from perfiles.models import Perfil

# logging # This retrieves a Python logging instance (or creates it)
import logging
logger = logging.getLogger(__name__)

def conversaciones(request):
    mensaje = ""
	# checkea el login del usuario
    username = ""
    chats = ""
    if request.user.is_authenticated:
        username = request.user.username
        chats_recibidos = Mensaje.objects.filter(usuario_dest = request.user).all()
        chats_enviados = Mensaje.objects.filter(usuario_rem = request.user).all()
        perfiles = Perfil.objects.all()
        logger.error("chats_recibidos: "+str(chats_recibidos))
        logger.error("chats_enviados: "+str(chats_enviados))
        logger.error("perfiles: "+str(perfiles))
        if request.method == "POST":
            mensajear = request.POST.get("mensajear")
            logger.error("mensajear: "+str(mensajear))
            if mensajear != None:
                return redirect('../mensajes/conversacion?id='+mensajear)
    else:
        return redirect('../login')
    context = {
		'mensaje':mensaje,
		'username':username,
        'enviados':chats_enviados,
        'recibidos':chats_recibidos,
        'perfiles':perfiles,
		'chats':chats,
	}
    return render(request, 'mensajes/conversaciones.html', context)

def conversacion(request):
    mensaje = ""
	# checkea el login del usuario
    username = ""
    chats = ""
    if request.user.is_authenticated:
        username = request.user.username
        iduser = str(request.GET.get("id"))
        logger.error("iduser: "+iduser)
        destinatario = User.objects.filter(id = iduser).first()
        user = Perfil.objects.filter(usuario = request.user).first()
        user_dest = Perfil.objects.filter(usuario = destinatario).first()
        if request.method == "POST":
            chatmensaje = request.POST.get("mensaje")
            chat = Mensaje.objects.create(
                usuario_rem = request.user,
                usuario_dest = destinatario,
                mensaje = chatmensaje,
            )
            chat.save()
        chats = Mensaje.objects.filter().all()
        logger.error("chats: "+str(chats))
    else:
        return redirect('../login')
    context = {
		'mensaje':mensaje,
		'username':username,
        'user':user,
        'destinatario':user_dest,
		'chats':chats,
	}
    return render(request, 'mensajes/conversacion.html', context)