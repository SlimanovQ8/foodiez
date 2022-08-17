from django import forms
from django.contrib.auth import get_user_model

from food import models

User = get_user_model()


class Registerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', "first_name", "email"]
        widgets ={
            "password": forms.PasswordInput()
        }
class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

class CategoryForm(forms.ModelForm):


    class Meta:
        model = models.Category
        exclude = ["created_by"]


class IngredientForm(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs= {'class': 'form-control'}),
            # 'image': forms.ImageField(attrs={'class': 'form-control'}),
            'category_name': forms.Select(attrs={'class': 'form-control'}),
        },

class RecipeForm(forms.ModelForm):


    class Meta:
        model = models.Recipe
        exclude = ["created_by"]

