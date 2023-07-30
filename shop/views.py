from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from .models import *

# Create your views here.

# def product_main(request):
#     products = Product.objects.all()
#     return render(request, 'shop/main.html', {'products' : products})

def product_detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    return render(request, 'shop/detail.html', {'product':product})

# 상품 메인 (전체 상품)
def main(request):
    products = Product.objects.filter(available_display=True)
    return render(request, 'shop/main.html', {'products':products})


# 상품 상세
# def product_detail(request, id, product_slug=None):
#     product = get_object_or_404(Product, id=id, slug=product_slug)
#
#     return render(request, 'shop/detail.html', {'product':product})


