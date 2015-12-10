from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from miapp.models import articulos,item,comentarios
from miapp.forms import comentariosForm
from django.shortcuts import get_object_or_404,render


# Create your views here.

def indice(request):
	lista_articulos = articulos.objects.values('tipo').distinct()
	return render (request, 'miapp/index.html', {'lista_articulos': lista_articulos})

def tipo(request,tipo_nombre):
	lista_articulos = articulos.objects.filter(tipo=tipo_nombre)
	return render (request, 'miapp/articulos.html', {'lista_articulos': lista_articulos,'tipo_nombre':tipo_nombre})


def tallas(request, articulo_id):
	if request.method == 'POST':
		form = comentariosForm(request.POST)
		if form.is_valid():
			comentario = form.save()
			comentario.usuario = request.user
			articulo = get_object_or_404(articulos, pk = articulo_id)
			comentario.articulos = articulo
			comentario.save()
			return HttpResponseRedirect("/item/"+articulo_id)
	else:
		lista_tallas = item.objects.filter(articulos=articulo_id)
		lista_comentarios = comentarios.objects.filter(articulos=articulo_id)
		form = comentariosForm()
		articulo = get_object_or_404(articulos, pk = articulo_id)
	return render (request, 'miapp/tallas.html', {'lista_tallas': lista_tallas,'form': form,'lista_comentarios': lista_comentarios, 'articulo': articulo})
	
	
def registro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "miapp/registro.html", {
'form': form,})

def loginpage(request):
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return HttpResponseRedirect("/")
	else:
		form = AuthenticationForm()
	return render(request,'miapp/login.html', {'form': form,})  

def logoutpage(request):
	logout(request)
	return HttpResponseRedirect("/")
