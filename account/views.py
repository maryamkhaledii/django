from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from account.forms import *
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import AuthenticationForm


class RegisterView(View):
    form = UserRegisterForm()
    template = "account/register.html"

    def get(self, request):
        return render(request, self.template, {"form": self.form})

    def post(self, request):
        st_form = UserRegisterForm(request.POST)
        if st_form.is_valid():
            new_user = User.objects.create_user(
                username=request.POST["username"],
                email="",
                password=request.POST["password"]
            )
            if new_user:
                return redirect("todo:home")
        return render(request, self.template,
                      {"form": self.form, "message": "یوزرنیم یا پسورد اشتباه یا تکراری است"}
                      )


class LoginView(View):
    form = UserLoginForm()
    template = "account/login.html"

    def get(self, request):
        return render(request, self.template, {"form": self.form})

    def post(self, request):
        form_data = UserLoginForm(request.POST)

        # if form_data.is_valid():
        user = authenticate(username=request.POST["username"],
                            password=request.POST["password"])

        if user and user.is_authenticated:
            login(request, user)
            return redirect("student:add-course")
        return render(request, self.template, {"form": self.form, "message": "یوزر یا پسورد اشتباه است"})


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect("account:user-login")
