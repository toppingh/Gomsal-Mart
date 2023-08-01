from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from accounts.forms import AccountAuthForm, RegistrationForm


def signUp(request, *args, **kwargs):
    user = request.user
    if user.is_authenticated:
        return HttpResponse("이미" +str(user.phonenum)+ "으로 로그인이 되어있습니다.")

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            raw_phonenum = form.cleaned_data.get('phonenum')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(phonenum=raw_phonenum, password=raw_password)
            login(request, account)
            destination = get_redirect_if_exists(request)
            if destination:
                return redirect(destination)
            return redirect('shop:main')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form'] = form

    return render(request, 'shop/signUp.html', context)

def logout(request):
    logout(request)
    return redirect("shop/main.html")

def Login(request, *args, **kwargs):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("shop/main.html")

    destination = get_redirect_if_exists(request)

    if request.POST:
        form = AccountAuthForm(request.POST)
        if form.is_valid():
            phonenum = request.POST.get('phonenum')
            password = request.POST.get('password')
            user = authenticate(phonenum=phonenum, password=password)
            if user:
                login(request, user)
                if destination:
                    return redirect(destination, "shop/main.html")
                return redirect("shop/main.html")
    else:
        form = AccountAuthForm()

    context['login_form'] = form
    return render(request, "shop/login_page.html", context)

def get_redirect_if_exists(request):
    redirect = None
    if request.GET:
        if request.GET.get("next"):
            redirect = str(request.GET.get("next"))
    return redirect


# from .forms import UserForm
#
#
# # Create your views here.
# #회원가입
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
#             auth.login(request, user)
#             return redirect('/')
#         return render(request, 'shop/signUp.html')
#     #
#     # else :
#     #     form = UserCreationForm()
#     #
#     # return render(request, 'shop/signUp.html', {'form': form})
#
# # class signUp(FormView):
# #     template_name = "shop/signUp.html"
# #     form_class = UserForm
# #     success_url = reverse_lazy("shop/main")
# #     def form_valid(self, form):
# #         form.save()
# #         username = form.cleaned_data.get("username")
# #         nickname = form.cleaned_data.get("nickname")
# #         birthY = form.cleaned_data.get("birthY")
# #         birthM = form.cleaned_data.get("birthM")
# #         birthD = form.cleaned_data.get("birthD")
# #         password = form.cleaned_data.get("password")
# #         phonenum = form.cleaned_data.get("phonenum")
# #         user = authenticate(form.request, nickname=phonenum, password=password)
# #         if user is not None:
# #             login(form.request, user)
# #         return super().form_valid(form)
#
# def logout(request):
#     auth.logout(request)
#     return redirect('home')
# #
# # def signup(request):
# #     return render(request, 'shop/signUp.html', {'signup': signup})
#
# def login(request):
#     if request.method == 'POST':
#         nickname = request.POST['nickname']
#         phonenum = request.POST['phonenum']
#         password = request.POST['password']
#         user = auth.authenticate(request, username=nickname or phonenum, password = password)
#         if user is not None:
#             auth.login(request, user)
#             return redirect('shop/main.html')
#         else:
#             return render(request, 'shop/login_page.html')
#     else:
#         return render(request, 'shop/login_page.html')
#
