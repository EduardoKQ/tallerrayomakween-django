from django.urls import path
from django.urls import include, path

from core import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('login', views.login, name='login'),
    path('trabajos', views.nuestros_trabajos, name='trabajos'),
    path('productos', views.productos, name='productos'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('auth_error', views.auth_error, name='auth_error'),
    path('admin_taller', views.admin_taller, name='admin_taller'),
    path('admin_trabajos', views.admin_trabajos, name='admin_trabajos'),
]