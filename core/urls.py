from django.urls import path
from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('login', views.login, name='login'),
    path('trabajos', views.nuestros_trabajos, name='trabajos'),
    path('productos', views.productos, name='productos'),
]