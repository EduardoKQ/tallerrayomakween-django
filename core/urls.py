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

    path('admin-taller', views.admin_taller, name='admin-taller'),
    path('admin-taller/nueva-cuenta', views.admin_taller_crearcuenta, name='admin-taller-crearcuenta'),
    path('admin-taller/actualizar-cuenta/<str:pk>', views.admin_taller_actualizarcuenta, name='admin-taller-actualizarcuenta'),
    path('admin-taller/borrar-cuenta/<str:pk>', views.admin_taller_borrarcuenta, name='admin-taller-borrarcuenta'),
    path('admin-taller/trabajos-pendientes', views.admin_taller_vertrabajos, name='admin-taller-vertrabajos'),

    path('admin_trabajos', views.admin_trabajos, name='admin-mecanico'),
]