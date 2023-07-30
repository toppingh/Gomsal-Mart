from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import UserForm


# Create your views here.
#회원가입
# def signUp(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2'] :
#             user = User.objects.create_user(
#                 username=request.POST['username'],
#                 password=request.POST['password1'],
#                 phonenum=request.POST['phonenum'],
#                 birthY=request.POST['birthY'],
#                 birthM=request.POST['birthM'],
#                 birthD=request.POST['birthD'],
#             )
#             auth.login(request.user)
#             return redirect('/')
#
#         return render(request, 'shop/signUp.html')
#
#     else :
#         form = UserCreationForm()
#
#     return render(request, 'shop/signUp.html', {'form': form})

class signUp(FormView):
    template_name = "shop/signUp.html"
    form_class = UserForm
    success_url = reverse_lazy("shop/main")
    def form_valid(self, form): # 👈 form을 전달받아옵니다.
        form.save() # 👈 form의 save() 매서드 실행
        username = form.cleaned_data.get("username")
        nickname = form.cleaned_data.get("nickname")
        birthY = form.cleaned_data.get("birthY")
        birthM = form.cleaned_data.get("birthM")
        birthD = form.cleaned_data.get("birthD")
        password = form.cleaned_data.get("password")
        phonenum = form.cleaned_data.get("phonenum")
        user = authenticate(form.request, nickname=phonenum, password=password)
        if user is not None:
            login(form.request, user)
        return super().form_valid(form)


def signup(request):
    return render(request, 'shop/signUp.html', {'signup': signup})
