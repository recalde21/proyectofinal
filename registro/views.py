from django.shortcuts import render, redirect
from .forms import UserCreationForm
from perfiles.models import Perfil

# logging # This retrieves a Python logging instance (or creates it)
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def register(request):
    form = UserCreationForm()
    if request.method == "POST":
		# Añado los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
		# Si el formulario es válido...
        if form.is_valid():
			# Creamos la nueva cuenta de usuario
            user = form.save()
            logger.error("form: "+str(form))
            perfil = Perfil.objects.create(
                usuario = user
            )
            perfil.save()
			# Si el usuario se crea correctamente
            return redirect('../login')
    # Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    # Si llegamos al final renderizamos el formulario
    context = {
		'form': form,
		#'mensaje': mensaje,
	}
    return render(request, "login-registro/register.html", context)
