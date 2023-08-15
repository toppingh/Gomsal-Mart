from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

import shop
from shop.models import Product
from django.http import JsonResponse

# Create your views here.


# @login_required #로그인 고쳐지면 수정
def favorite_products(request):
    user = request.user
    favorite_products = user.favorite_products.all()  # 'favorite_products'는 User 모델에서 정의한 related_name

    context = {
        'favorite_products': favorite_products,
    }

    return render(request, 'favorites.html', context)



def update_summary(request):
    if request.method == 'POST':
        # POST 요청으로부터 데이터 추출
        item_indexes = request.POST.getlist('itemIndex')
        quantities = request.POST.getlist('quantity')

        total_amount = 0
        item_count = 0

        for item_index, quantity in zip(item_indexes, quantities):
            item = Product.objects.get(pk=item_index)
            price = item.price
            total_amount += price * int(quantity)
            item_count += 1

        return render(request, 'your_template.html', {'item_count': item_count, 'total_amount': total_amount})

    from django.shortcuts import redirect
    from django.views.decorators.http import require_POST
    from .models import Product
    from .forms import UpdateQuantityForm

    @require_POST
    def update_quantity(request):
        form = UpdateQuantityForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            new_quantity = form.cleaned_data['new_quantity']

            # 상품 정보 가져오기
            product = Product.objects.get(id=product_id)

            # 수량 업데이트
            product.stock = new_quantity
            product.save()

            # 선택 상품 목록 페이지로
            return redirect('shop/bookmark_page.html')