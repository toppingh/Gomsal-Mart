from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def product_main(request):
    products = Product.objects.all()
    return render(request, 'shop/main.html', {'products' : products})

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)

    return render(request, 'shop/detail.html', {'product':product})