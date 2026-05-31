from django.contrib.auth import logout
# from django.contrib.auth.decorators import login_required
# from allauth.account.forms import LoginForm
# from django.shortcuts import render
# from .forms import RegisterForm, LoginForm
from django.shortcuts import redirect, render
from django.urls import reverse


# Create your views here.
from django.shortcuts import render,  reverse
from allauth.account.forms import LoginForm
from .forms import CustomersForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST, request=request)

        if form.is_valid():
            form.login(request)
            return redirect(reverse("shop:home"))
        else:
            return render(request, 'acounts/login.html', {'error': form.errors})

    return render(request, 'acounts/login.html')

# def login_view(req):
#     if not req.user.is_authenticated:
#         print(req)
#         if req.method == "POST":
#             print("post")
#             form = LoginForm(data=req.POST)
#             if form.is_valid():
#                 form.login(req)
#                 return reverse("/")
#         print("not valid")
#         return render(req, "acounts/login.html")
#     return reverse("/")


def register_view(request):
    if request.method == "POST":
        form = CustomersForm(request.POST)
        if form.is_valid():
            return redirect(reverse("shop:home"))
        else:
            return render(request, "acounts/register.html", {"error": form.errors})

    return render(request, "acounts/register.html")


def logout_view(request):
    print("this view called!")
    if request.user.is_authenticated:
        print("logouting")
        logout(request)
        print("this user loged out!")
    print("this line is working")
    return redirect(reverse("shop:home"))
