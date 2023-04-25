from django.shortcuts import render, redirect

# logging # This retrieves a Python logging instance (or creates it)
import logging
logger = logging.getLogger(__name__)

# Login / Register
from django.contrib.auth import authenticate
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from login.forms import AuthenticationForm

from blog import views

def login(request):
    mensaje = ""
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        logger.error("form: "+str(form))
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            logger.error("password: "+str(raw_password))
            user = authenticate(username=username, password=raw_password)
            do_login(request, user)
            if user.is_staff:
                return redirect("/admin")
            else:
                return redirect("/profile")
        else:
            mensaje = "Datos incorrectos."
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
        'mensaje':mensaje,
    }
    return render(request, 'login-registro/login.html', context)

def logout(request):
	# Finalizamos la sesión
	do_logout(request)
	# Redireccionamos a la portada
	return redirect('/')