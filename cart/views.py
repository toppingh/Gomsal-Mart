from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product
from .forms import AddCartForm
from .cart import Cart

# Create your views here.
@require_POST
def add(request, product_id): # 장바구니에 담기
    cart = Cart(request) # 장바구니 객체 생성
    product = get_object_or_404(Product, id=product_id) # 상품 정보 전달

    form = AddCartForm(request.POST) # 추가되는 상품 정보느 상세 페이지나 장바구니 페이지로부터 전달되어 이 폼을 통해 만들어진 데이터이다.
    if form.is_valid():
        cd = form.cleaned_data
        # 장바구니에 상품과 해당 상품의 수량을 더하고 상세 화면인지 장바구니 화면인지에 따라 방식을 다르게 한다.
        cart.add(product=product, quantity=cd['quantity'], is_update=['is_update'])

    return redirect('cart:cart') # 뷰 동작 시 장바구니 화면을 보여준다.

# 장바구니에서 삭제하기
def remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart') # 뷰 동작 시 장바구니 화면을 보여준다.

# 장바구니 화면을 볼 수 있는 뷰
def detail(request):
    cart = Cart(request)

    # 노출될 상품을 장바구니 객체인 cart로부터 가져온다.
    for product in cart:
        # 상품의 수량 (수정) = 폼을 이용해서 상품마다 하나씩 추가하는데 수정하는대로 반영해야 하므로 is_update=True
        product['quantity_form'] = AddCartForm(initial={'quantity':product['quantity'], 'is_update':True})
    return render(request, 'cart/cart.html', {'cart':cart})