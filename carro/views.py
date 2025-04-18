from django.shortcuts import render
from .carro import Carro
from eafit_comercio.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)

    carro.agregar(producto = producto)

    return redirect("Eafit_comercio")


def eliminar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)

    carro.eliminar(producto = producto)

    return redirect("Eafit_comercio")


def restar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)

    carro.restar_producto(producto = producto)

    return redirect("Eafit_comercio")


def limpiar_carro(request, producto_id):

    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("Eafit_comercio")


