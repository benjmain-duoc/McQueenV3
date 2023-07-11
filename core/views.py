from django.shortcuts import render
from argparse import Action
from django.shortcuts import render,redirect
from .models import Producto ,Categoria
from .forms import  ProductoForm
# Create your views here.

def inicio(request):
    return render(request, "core/inicio.html")


def agregar_tarjeta(request):
    return render(request, "core/agregar_tarjeta.html")


def equipo(request):
    return render(request, "core/Equipo.html")


def ingresar(request):
    return render(request, "core/ingresar.html")


def metodos_pagos(request):
    return render(request, "core/metodos_pagos.html")


def nosotros(request):
    return render(request, "core/nosotros.html")


def registro(request):
    return render(request, "core/Registro.html")


def S_ajustes(request):
    return render(request, "core/S_ajuste.html")


def S_cambio(request):
    return render(request, "core/S_cambio.html")


def S_lamina(request):
    return render(request, "core/S_lamina.html")


def S_mantencion(request):
    return render(request, "core/S_mantencion.html")


def S_pintura(request):
    return render(request, "core/S_pintura.html")


def S_polarizado(request):
    return render(request, "core/S_polarizado.html")


def S_todos(request):
    return render(request, "core/S_todos.html")

#======================================================
#======================================================
#======================================================
#======================================================


def ficha(request, id_producto):
    producto = Producto.objects.get(id_producto=id_producto)
    data = {"producto":  producto}
    return render(request, "core/ficha_producto.html", data)

def tienda(request):
    data = {"list": Producto.objects.all().order_by('id_producto')}
    return render(request, "core/tienda_producto.html", data)


def producto(request, action, id_producto):
    data = {"mesg": "", "form": ProductoForm, "action": action, "id_producto": id_producto}

    if action == 'ins':
        if request.method == "POST":
            form = ProductoForm(request.POST, request.FILES)
            if form.is_valid:
                try:
                    form.save()
                    data["mesg"] = "¡Producto agregado!"
                except:
                    data["mesg"] = "¡Error al agregar el producto!"

    elif action == 'upd':
        objeto = Producto.objects.get(id_producto=id_producto)
        if request.method == "POST":
            form = ProductoForm(data=request.POST, files=request.FILES, instance=objeto)
            if form.is_valid:
                form.save()
                data["mesg"] = "¡Producto actualizado!"
        data["form"] = ProductoForm(instance=objeto)

    elif action == 'del':
        try:
            Producto.objects.get(id_producto=id_producto).delete()
            data["mesg"] = "¡Producto eliminado!"
            return redirect(producto, action='ins', id_producto = '-1')
        except:
            data["mesg"] = "¡Producto no existe!"

    data["list"] = Producto.objects.all().order_by('id_producto')
    return render(request, "core/producto.html", data)

def poblar(request):
    Producto.objects.all().delete()
    Producto.objects.create(id_producto=1, producto='Liquido de frenos', detalles="Liquido de freno 237 ML WAGNER Diseñado para ofrecer una frenada precisa y confiable, este liquido de freno es la elección ideal para mantener tu sistema de frenado en óptimas condiciones.", imagen="images/liquidodefreno.jpg", categoria=Categoria.objects.get(id_Categoria=2))
    Producto.objects.create(id_producto=2, producto='Aceite Mobil', detalles="Optimiza el rendimiento y protege el motor de tu vehículo con el aceite especial de la reconocida marca Mobil.", imagen="images/mobil_especial.jpg", categoria=Categoria.objects.get(id_Categoria=2))
    Producto.objects.create(id_producto=3, producto='Neumaticos', detalles="Experimenta la máxima potencia y agarre en la carretera con nuestros neumáticos deportivos de alto rendimiento, TRACCION Y DURABILIDAD.", imagen="images/neumatico.jpg", categoria=Categoria.objects.get(id_Categoria=1))
    Producto.objects.create(id_producto=4, producto='Parachoques 4X4', detalles="Barricade Trail Force Parachoques delantero con luces LED compatible con Jeep Wrangler ademas brinda una gran estetica y una grann funcionalidad", imagen="images/para_.jpg", categoria=Categoria.objects.get(id_Categoria=1))
    Producto.objects.create(id_producto=5, producto='Aleron', detalles="Maximiza el rendimiento aerodinámico y dale un aspecto deportivo a tu vehículo con nuestro alerón de alta calidad. Diseñado con precisión y estilo, este alerón no solo mejora la estabilidad y la tracción en carretera", imagen="images/aleron.jpeg", categoria=Categoria.objects.get(id_Categoria=1))
    Producto.objects.create(id_producto=6, producto='Tubo de escape', detalles="Mejora el rendimiento y el estilo de tu vehículo con nuestro tubo de escape de alta calidad. Diseñado para ofrecer un flujo de gases óptimo y un sonido deportivo", imagen="images/tubo.png", categoria=Categoria.objects.get(id_Categoria=1))

    return redirect(producto, action='ins', id_producto = '-1')