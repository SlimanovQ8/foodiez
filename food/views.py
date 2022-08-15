from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from food import forms
from food import models
# Create your views here.
def home_Page(request):
    categories: list[models.Category] = list(models.Category.objects.all())

    context = {
        "categories": categories,
    }

    return render(request, "home_page.html", context)

def register_user(request):
    print("hi")
    form = forms.Registerform()
    print(form)
    if request. method == "POST":
        form = forms.Registerform(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(user. password)
            user.save()
            login(request, user)
            return redirect("home")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def login_page(request):
    form = forms.UserLogin()
    if request.method == "POST":
        form = forms.UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username)
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("home")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)


def create_category(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    print("1er5tdgfc6tygfhvn ")
    form = forms.CategoryForm()
    if request.method == "POST":
        # BONUS: This needs to have the `user` injected in the constructor
        # somehow
        form = forms.CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            categor = form.save(commit=False)
            categor.created_by = request.user
            categor.save()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_category.html", context)

