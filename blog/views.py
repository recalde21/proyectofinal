from django.shortcuts import render, redirect
from .models import Blog

# logging # This retrieves a Python logging instance (or creates it)
import logging
logger = logging.getLogger(__name__)

from .forms import PageCreationForm#, PageChangeForm

def home(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	context = {
		'mensaje':mensaje,
		'username':username,
		}
	return render(request, 'blog/home.html', context)

def blogs(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	else:
		return redirect('login')
	# obtengo los blogs de la base de datos
	blogs = Blog.objects.filter(deleted = False).all()
	context = {
		'mensaje':mensaje,
		'blogs':blogs,
		'username':username,
		}
	return render(request, 'blog/pages.html', context)

def about(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	context = {
		'mensaje':mensaje,
		'username':username,
		}
	return render(request, 'blog/about.html', context)

def page(request):
	mensaje = ""
	pagina = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	idp = str(request.GET.get("id"))
	logger.error("idp: "+idp)
	if idp != "":
		pagina = Blog.objects.filter(id = idp, deleted = False).first()
	else:
		return redirect("../pages")
	if request.method == "POST":
		mensajear = request.POST.get("mensajear")
		logger.error("mensajear: "+str(mensajear))
		if mensajear != None:
			return redirect("../mensajes/conversacion?id="+mensajear)
	logger.error("pagina: "+str(pagina))
	context = {
		'mensaje':mensaje,
		'username':username,
		'pagina':pagina,
		}
	return render(request, 'blog/page.html', context)

def createpage(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	else:
		return redirect('login')
	if request.method == "POST":
		form = PageCreationForm(request.POST, request.FILES)
		logger.error("form: "+str(form))
		if form.is_valid():
			# guardo la page
			formpage = form.save(commit=False)
			#logger.error("page.imagen: "+str(page.imagen))
			page = Blog.objects.create(
                titulo = formpage.titulo,
                subtitulo = formpage.subtitulo,
                cuerpo = formpage.cuerpo,
                autor = request.user,
                imagen = formpage.imagen
            )
			page.save()
			mensaje = "Página creada."
	form = PageCreationForm()
	context = {
		'mensaje':mensaje,
		'username':username,
        'form':form,
		'mensaje':mensaje,
	}
	return render(request, 'blog/createpage.html', context)

def updatepage(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
		idp = request.GET.get("id")
		page = Blog.objects.filter(id = idp, autor = request.user).first()
		#form = PageChangeForm(request.POST, request.FILES)
		form = PageCreationForm(request.POST, request.FILES)
		logger.error("form: "+str(form))
		if form.is_valid():
			formpage = form.save(commit=False)
			page.titulo = formpage.titulo
			page.subtitulo = formpage.subtitulo
			page.cuerpo = formpage.cuerpo
			page.imagen = formpage.imagen
			page.save()
			return redirect("../profile")
		else:
			#mensaje = "Datos inválidos."
			#form = PageChangeForm()
			form = PageCreationForm()
	else:
		return redirect('login')
	context = {
		'mensaje':mensaje,
		'username':username,
		'form':form,
	}
	return render(request, 'blog/updatepage.html', context)

# sin uso
def deletepage(request):
	mensaje = ""
	# checkea el login del usuario
	username = ""
	if request.user.is_authenticated:
		username = request.user.username
	else:
		return redirect('login')
	context = {
		'mensaje':mensaje,
		'username':username,
		}
	return render(request, 'blog/deletepage.html', context)