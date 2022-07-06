from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .models import User


def sign_in(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                name=request.POST["name"],
                nickname=request.POST["nickname"],
                email=request.POST["email"],
                password=request.POST["password1"],
            )
            login(request, user)
            return redirect("post:post_list")
        else:
            messages.error(request, "passwords are incorrect.")
            return render(
                request, "user/signin.html", {"error": "passwords are incorrect."}
            )
    else:
        return render(request, "user/signin.html")


def log_in(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("post:post_list")
        else:
            return render(
                request,
                "user/login.html",
                {"error": "e-mail or password is incorrect."},
            )
    else:
        return render(request, "user/login.html")


def log_out(request):
    logout(request)
    return redirect("post:post_list")


# Create your views here.
