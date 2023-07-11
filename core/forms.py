from django import forms 
from django.forms import ModelForm, fields
from .models import Producto

#class UsuarioForms(ModelForm):
    #class Meta:
       # model = Usuario
        #fields = ['id_cliente','nombre','email','rut','direccion','ciudad']

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['id_producto', 'producto', 'detalles', 'imagen', 'categoria']