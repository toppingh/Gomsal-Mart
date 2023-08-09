from django.shortcuts import render, redirect
from django.utils import timezone

from comment.forms import CommentForm
from comment.models import Comment


# Create your views here.

#리뷰 달기
def add_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('/')  # 댓글을 단 상품의 상세 페이지로 이동... 추후 수정
    else:
        form = CommentForm()
    return render(request, 'comment/add_comment.html', {'form': form})

#평균 별점 계산
def detail_view(request):
    # 모든 사용자의 댓글 별점 조회..
    all_ratings = Comment.objects.filter(rating__isnull=False).values_list('rating', flat=True)

    # 별점의 평균 계산
    if all_ratings:
        average_rating = sum(all_ratings) / len(all_ratings)
    else:
        average_rating = 0

    context = {
        'average_rating': average_rating,
    }

    return render(request, 'shop/detail.html', context)