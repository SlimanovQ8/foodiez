from django.contrib import admin

# Register your models here.
from .models import Category, Ingredient, Recipe, UserProfile
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(UserProfile)