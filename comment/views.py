from django.shortcuts import render, redirect
from django.utils import timezone

from comment.forms import CommentForm
from comment.models import Comment


# Create your views here.


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

