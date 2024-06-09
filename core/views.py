from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def nosotros(request):
    template = loader.get_template('nosotros.html')
    return HttpResponse(template.render({}, request))

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

def nuestros_trabajos(request):
    template = loader.get_template('trabajos.html')
    return HttpResponse(template.render({}, request))

def productos(request):
    template = loader.get_template('productos.html')
    return HttpResponse(template.render({}, request))