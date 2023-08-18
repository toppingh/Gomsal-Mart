from django.http import JsonResponse
from django.shortcuts import render, redirect

from search.models import SearchHistory
from shop.models import Product
from django.db.models import Q

# Create your views here.
def searchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))

        if request.user.is_authenticated:  # 로그인한 사용자인 경우에만 기록...
            SearchHistory.objects.create(user=request.user, query=query)

    return render(request, 'shop/product_list_page.html', {'query':query, 'products':products})


def clear_search_history(request):
    if request.user.is_authenticated:
        request.user.searchhistory_set.all().delete()