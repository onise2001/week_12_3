from django.shortcuts import render, redirect
from .models import Recipe

# Create your views here.

def index(request):

    recipes = Recipe.objects.all()
    return render(request, 'recepie_manager/index.html', {"recipes": recipes})


def add_recipe(request):
    if request.method == "POST":
        name = request.POST.get("name")
        ingredients = request.POST.get("ingredients")
        instructions = request.POST.get("instructions")
        recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
        recipe.save()
    
    return render(request, "recepie_manager/add_recipe.html")




def show_recipe(request, id):
    recipe = Recipe.objects.filter(pk=id)
    return render(request, "recepie_manager/recipe.html", {"recipe": recipe[0]})