from django.shortcuts import render
from negocear.models import Post, Categoria


# Create your views here.


def negoseo(request):

    posts = Post.objects.all()
    return render(request, "negocear/negoseo.html", {"posts": posts})


def categoria(request, categoria_id):

    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias = categoria)

    return render(request, 'negocear/categoria.html', {'categoria':categoria, 'posts':posts})