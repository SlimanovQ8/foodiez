from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from food import forms
from food import models
# Create your views here.
def home_Page(request):
    categories: list[models.Category] = list(models.Category.objects.all())

    context = {
        "categories": categories,
    }

    return render(request, "home_page.html", context)
def recipes(request):
    recipes: list[models.Recipe] = list(models.Recipe.objects.all())

    context = {
        "recipes": recipes,
    }

    return render(request, "recipes.html", context)
def category_detail(request, CategoryID):
    category = models.Category.objects.get(id=CategoryID)
    ingredient: list[models.Category.objects.get(id= CategoryID)] = list(category.ingredients.all())
    context = {
        "categories": {
            "name": category.name,
            "description": category.description,
            "image": category.image,
            "NumOfIngredients": len(ingredient),

        },
        "ingredients": ingredient

    }

    return render(request, "category_detail.html", context)
def recipe_detail(request, RecipeID):
    Rec = models.Recipe.objects.get(id=RecipeID)
    ingredient: list[models.Recipe.objects.get(id= RecipeID)] = list(Rec.ingredients.all())

    context = {
        "recipe": {
            "name": Rec.name,
            "description": Rec.description,
            "image": Rec.image,
            "instructions": Rec.instruction,
            "chalories": Rec.chalories,
            "NumOfIngredients": len((ingredient)),

        },
         "ingredients": ingredient

    }

    return render(request, "recipe_detail.html", context)

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

def logout_view(request):
    logout(request)
    return redirect("home")

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
            categor = form.save(commit=False) # Wait dont save
            categor.created_by = request.user # assign the created by to the user
            categor.save()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_category.html", context)


def create_ingredient(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    print("1er5tdgfc6tygfhvn ")
    form = forms.IngredientForm()
    if request.method == "POST":
        # BONUS: This needs to have the `user` injected in the constructor
        # somehow
        form = forms.IngredientForm(request.POST, request.FILES)

        if form.is_valid():
            ing = form.save(commit=False)
            ing.save()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_ingredients.html", context)

def create_recipe(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    print("1er5tdgfc6tygfhvn ")
    form = forms.RecipeForm()
    if request.method == "POST":

        form = forms.RecipeForm(request.POST, request.FILES)

        if form.is_valid():
            rec = form.save(commit=False)
            rec.created_by = request.user
            rec.save()
            form.save_m2m()
            print("printing here!", rec)
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_recipe.html", context)
