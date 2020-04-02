from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse
from .models import Product


# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {
        'user' : request.user,
        'products' : products
    }
    return render(request, 'index.html' , context)


def product(request, id):
    # query = Product.objects.get(id=id)
    query = get_object_or_404(Product, id=id)
    context = {
        'product': query
    }
    return render(request, 'product.html', context)


def error404(request, exception):
    template = loader.get_template('404.html')
    return HttpResponse(
        content=template.render(), 
        content_type='text/html; charset=utf8', 
        status=404
    )


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(
        content=template.render(), 
        content_type='text/html; charset=utf8', 
        status=500
    )