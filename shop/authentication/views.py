from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render


def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect("Goods")  # TODO modify redirect url


def login_user(request: HttpRequest) -> HttpResponse:
    auth_form = AuthenticationForm(request, request.POST)

    if request.user.is_authenticated:
        return redirect("Goods")  # TODO modify redirect url
    if request.method == "POST":
        if auth_form.is_valid():
            user = auth_form.get_user()
            login(request, user)
            return redirect("Goods")  # TODO modify redirect url

    return render(
        request,
        "login.html",
        context={
            "auth_form": auth_form,
        }
    )


def register_user(request: HttpRequest) -> HttpResponse:
    register_form = UserCreationForm(request.POST)

    if request.method == "POST" and register_form.is_valid():
        register_form.save()
        return redirect("login")

    return render(
        request,
        "register.html",
        context={
            "register_form": register_form,
        }
    )
