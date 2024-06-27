from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.template import loader

from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import Group, User

from . import models
from .forms import RegisterClienteForm, MecanicoForm, UserForm
from .decorators import unauthenticated_user, allowed_users
from .models import Mecanico


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def nosotros(request):
    template = loader.get_template('nosotros.html')
    return HttpResponse(template.render({}, request))


#@unauthenticated_user
def login(request):
    register_form = RegisterClienteForm()
    context = {'register_form': register_form}
    template = loader.get_template('login.html')

    if request.method == 'POST':
        if "register" in request.POST:
            user_creation_form = RegisterClienteForm(request.POST)
            if user_creation_form.is_valid():
                #creamos el usuario de forma manual
                user = User.objects.create_user(username=user_creation_form.cleaned_data['email'],
                                                email=user_creation_form.cleaned_data['email'],
                                                password=user_creation_form.cleaned_data['password1'],
                                                first_name=user_creation_form.cleaned_data['first_name'],)

                # asignamos el grupo "cliente"
                group_cliente = Group.objects.get(name='cliente')
                user.groups.add(group_cliente)

                user.save()
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

# Vistas del Administrador del Taller
@allowed_users(allowed_roles=['administrador_taller'])
def admin_taller(request):
    context={
        "mecanicos" : Mecanico.objects.all(),
    }
    return render(request,"admin-taller.html",context)
@allowed_users(allowed_roles=['administrador_taller'])
def admin_taller_crearcuenta(request):
    mecanico_form = MecanicoForm()
    user_form = UserForm()
    if request.method == "POST":
        mecanico_form = MecanicoForm(request.POST, prefix='mecanico_form')
        user_form = UserForm(request.POST, prefix='user_form')
        #print(1)
        #print(mecanico_form.is_valid(), user_form.is_valid())
        if mecanico_form.is_valid() and user_form.is_valid():
            #print(2)
            #creamos el nuevo usuario
            user = User.objects.create_user(username=user_form.cleaned_data['email'],
                                            email=user_form.cleaned_data['email'],
                                            password=user_form.cleaned_data['password1'],
                                            first_name=mecanico_form.cleaned_data['nombre'], )
            # asignamos el grupo "cliente"
            group_mecanico = Group.objects.get(name='mecanico')
            user.groups.add(group_mecanico)
            user.save()
            #creamos el mecanico y asignamos su usuario
            mecanico = Mecanico.objects.create(user=user,
                                               rut=mecanico_form.cleaned_data['rut'],
                                               nombre=mecanico_form.cleaned_data['nombre'],
                                               telefono=mecanico_form.cleaned_data['telefono'],
                                               fecha_nacimiento=mecanico_form.cleaned_data['fecha_nacimiento'],
                                               direccion=mecanico_form.cleaned_data['direccion'],
                                               especialidad=mecanico_form.cleaned_data['especialidad']
                                               )
            mecanico.save()
            return redirect("/admin-taller")

    context = {"user_form": user_form,
               'mecanico_form': mecanico_form}
    return render(request, "admin-taller-crearcuenta.html", context)

@allowed_users(allowed_roles=['administrador_taller'])
def admin_taller_actualizarcuenta(request, pk):
    mecanico = Mecanico.objects.get(rut=pk)
    user = mecanico.user

    mecanico_form = MecanicoForm(instance=mecanico)

    if request.method == "POST":
        mecanico_form = MecanicoForm(request.POST, instance=mecanico)
        if mecanico_form.is_valid():
            mecanico_form.save()
            return redirect("/admin-taller")

    context = {'mecanico_form': mecanico_form}
    return render(request, "admin-taller-crearcuenta.html", context)

@allowed_users(allowed_roles=['administrador_taller'])
def admin_taller_borrarcuenta(request, pk):
    mecanico = Mecanico.objects.get(rut=pk)
    user = mecanico.user
    context ={"mecanico" : mecanico,
              "user" : user
              }

    if request.method == "POST":
        print(mecanico)
        #user.delete()
        #mecanico.delete()
        return redirect("/admin-taller")

    return render(request, "admin-taller-borrarcuenta.html", context)


@allowed_users(allowed_roles=['administrador_taller'])
def admin_taller_vertrabajos(request):
    return None


@allowed_users(allowed_roles=['mecanico'])
def admin_trabajos(request):
    template = loader.get_template('admin-mecanico.html')
    return HttpResponse(template.render({}, request))