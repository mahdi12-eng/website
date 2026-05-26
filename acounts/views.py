from django.shortcuts import render

# Create your views here.


def login_view(request):
    if request.method == "POSt":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(url(index))
    form = LoginForm()
    return render(request, "shop/login.html")


def register_view(request):
    if request.method == "POST":
        form = CustomersForm(request.POST)
        print("post request")
        if form.is_valid():
            print("form is valid ")
            form.save()
            return redirect(url(index))
    form = CustomersForm(request.POST)
    return render(request, "shop/register.html", {"form": form})
