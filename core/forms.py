from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Mecanico

class RegisterClienteForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name',"email", 'password1', 'password2']


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", 'password1', 'password2']
class MecanicoForm(forms.ModelForm):
    class Meta:
        model = Mecanico
        fields = [
            "rut",
            "nombre",
            "telefono",
            "fecha_nacimiento",
            "direccion",
            "especialidad"
        ]

