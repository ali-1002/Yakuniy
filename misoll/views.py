from django.shortcuts import render, get_object_or_404, redirect
from .models import FoodModel
from django.db.models import Q
from .forms import FoodModelForm, RecipeModelForm

def food_view(request):
    food_obj = get_object_or_404(FoodModel, id=id)
    return render(request, template_name='food_view.html', context={
        'food': food
    
    })
