from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader

from django.contrib.auth import authenticate, login as auth_login, logout

from .forms import RegisterClienteForm

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def nosotros(request):
    template = loader.get_template('nosotros.html')
    return HttpResponse(template.render({}, request))

def login(request):
    if request.user.is_authenticated:
        return redirect('/')

    register_form = RegisterClienteForm()
    context = {'register_form': register_form}
    template = loader.get_template('login.html')

    if request.method == 'POST':
        if "register" in request.POST:
            user_creation_form = RegisterClienteForm(request.POST)
            if user_creation_form.is_valid():
                user_creation_form.save()
                messages.success(request, 'Registrado con exito!')
                return redirect("/login")

        if "login" in request.POST:
            username = request.POST['login_email']
            password = request.POST['login_password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login exitoso!')
                return redirect("/")
            else:
                messages.info(request, "Correo o Contraseña incorrectos")

    return HttpResponse(template.render(context, request))

def user_logout(request):
    logout(request)
    return redirect('/')
def nuestros_trabajos(request):
    template = loader.get_template('trabajos.html')
    return HttpResponse(template.render({}, request))

def productos(request):
    template = loader.get_template('productos.html')
    return HttpResponse(template.render({}, request))