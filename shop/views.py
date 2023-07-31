from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404

from .models import *
from cart.forms import AddCartForm

# Create your views here.
# 상품 메인 (전체 상품)
def main(request):
    products = Product.objects.filter(available_display=True)
    return render(request, 'shop/main.html', {'products':products})

# 상품 상세 -> 장바구니 구현 후 장바구니 담기 추가
def detail(request, id, product_slug=None):
    product = get_object_or_404(Product, id=id, slug=product_slug)
    # 장바구니 담기 기능 활성화를 위해 뷰 슈정
    add_to_cart = AddCartForm(initial={'quantity':1})
    return render(request, 'shop/detail.html', {'product':product, 'add_to_cart':add_to_cart})


