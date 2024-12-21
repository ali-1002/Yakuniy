from django import forms
from .models import RecipeModel, FoodModel

class FoodModelForm(forms.ModelForm):
    class Meta:
        model = FoodModel
        fields = ['name', 'price', 'recipes']

class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        fields = ['product', 'dickraption']