from django.shortcuts import render
from .models import Producto

# Create your views here.

def eafit_comercio(request):

    productos = Producto.objects.all()

    return render(request, "eafit_comercio/eafit_comercio.html", {"productos": productos})