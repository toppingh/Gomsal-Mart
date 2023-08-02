from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', detail, name='detail'), # 장바구니 페이지
    path('add/<int:product_id>', add, name='product_add'), # 추가
    path('remove/<product_id>', remove, name='product_remove'), # 삭제
]