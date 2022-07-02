from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Cliente


class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['rut', 'nombre', 'correo', 'telefono', 'direccion']
        labels = {
            'rut': 'Rut',
            'nombre': 'Nombre',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',

        }
        widgets = {
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese rut',
                    'id': 'rut'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese nombre',
                    'id': 'nombre'
                }
            ),
            'correo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese correo',
                    'id': 'correo'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'telefono',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese direccion',
                    'id': 'direccion'
                }
            )

        }
