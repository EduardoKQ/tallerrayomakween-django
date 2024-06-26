from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import Group

from .forms import RegisterClienteForm
from .decorators import unauthenticated_user, allowed_users

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def nosotros(request):
    template = loader.get_template('nosotros.html')
    return HttpResponse(template.render({}, request))


@unauthenticated_user
def login(request):
    register_form = RegisterClienteForm()
    context = {'register_form': register_form}
    template = loader.get_template('login.html')

    if request.method == 'POST':
        if "register" in request.POST:
            user_creation_form = RegisterClienteForm(request.POST)
            if user_creation_form.is_valid():

                user = user_creation_form.save()
                group_cliente = Group.objects.get(name='cliente')
                user.groups.add(group_cliente)

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

def auth_error(request):
    group = request.user.groups.all()[0].name
    print(group)
    if group == "administrador_taller":
        return redirect("/admin_taller")
    if group == "cliente":
        return redirect("/")
    if group == "mecanico":
        return redirect("/admin_trabajos")

    if group == "superuser":
        return redirect("/admin")

    return redirect("/")

def nuestros_trabajos(request):
    template = loader.get_template('trabajos.html')
    return HttpResponse(template.render({}, request))

def productos(request):
    template = loader.get_template('productos.html')
    return HttpResponse(template.render({}, request))

@allowed_users(allowed_roles=['administrador_taller'])
def admin_taller(request):
    template = loader.get_template('nosotros.html')
    return HttpResponse(template.render({}, request))
@allowed_users(allowed_roles=['mecanico'])
def admin_trabajos(request):
    template = loader.get_template('productos.html')
    return HttpResponse(template.render({}, request))