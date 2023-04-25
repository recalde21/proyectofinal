from django.shortcuts import render, redirect
from .forms import UserChangeForm, ProfileChangeForm
from .models import Perfil
from blog.models import Blog

# logging # This retrieves a Python logging instance (or creates it)
import logging
logger = logging.getLogger(__name__)

# Create your views here.
def profile(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	paginas = ""
	perfil = None
	if request.user.is_authenticated:
		if request.method == "POST":
			editar = request.POST.get("editar")
			idp_eliminar = request.POST.get("eliminar")
			logger.error("editar: "+str(editar))
			logger.error("idp_eliminar: "+str(idp_eliminar))
			if editar != None:
				return redirect("../updatepage?id="+editar)
			elif idp_eliminar != None:
				pagina = Blog.objects.filter(id=idp_eliminar).first()
				pagina.deleted = True
				pagina.save()
		username = request.user.username
		perfil = Perfil.objects.filter(usuario = request.user, deleted = False).first()
		paginas = Blog.objects.filter(autor = request.user, deleted = False).all()
		logger.error("perfil.link: "+str(perfil.link))
		if perfil is None:
			return redirect('../login')
	else:
		return redirect('../login')
	context = {
		'mensaje':mensaje,
		'username':username,
		'perfil':perfil,
		'paginas':paginas,
		}
	return render(request, 'perfil/profile.html', context)

def editprofile(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
		if request.method == "POST":
			#form = UserChangeForm(data=request.POST)
			form = ProfileChangeForm(request.POST, request.FILES)
			logger.error("form: "+str(form))
			if form.is_valid():
				formperfil = form.save(commit=False)
				#logger.error("formperfil: "+str(formperfil))
				perfil = Perfil.objects.filter(usuario = request.user).first()
				perfil.link = formperfil.link
				perfil.descripcion = formperfil.descripcion
				perfil.imagen = formperfil.imagen
				logger.error("el form es valido")
				perfil.save()
				return redirect("../profile")
			else:
				mensaje = "Datos inválidos."
		else:
			#form = UserChangeForm()
			form = ProfileChangeForm()
	else:
		return redirect('../login')
	context = {
		'mensaje':mensaje,
		'username':username,
        'user':request.user,
		'form':form,
	}
	return render(request, 'perfil/editprofile.html', context)