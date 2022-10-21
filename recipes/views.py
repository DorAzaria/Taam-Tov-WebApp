from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Recipe, Tag
from .forms import RecipeForm, CommentForm, RecipeIngredientForm, RecipeMethodForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchRecipes , paginateRecipes
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def recipes(request):
    recipes, search_query = searchRecipes(request)
    custom_range, recipes = paginateRecipes(request, recipes, 6)

    context = {'recipes': recipes,
               'search_query': search_query, 'custom_range': custom_range}
    return render(request, 'recipes/recipes.html', context)

# pk = primary key (str type)
def recipe(request, pk):
    recipeObj = Recipe.objects.get(id=pk)
    form = CommentForm()
    recipeObj.getViews

    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.recipe = recipeObj
        comment.owner = request.user.profile

        comment.save()

        recipeObj.getLikesCount
        messages.success(request, 'התגובה שלך פורסמה בהצלחה!')
        return redirect('recipe', pk=recipeObj.id)

    return render(request, 'recipes/single-recipe.html', {'recipe': recipeObj,'form': form})

@login_required(login_url="login")
def createRecipe(request):
    profile = request.user.profile
    form = RecipeForm()

    if request.method == 'POST' :
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            return redirect('account')

    context = {'form': form}
    return render(request, "recipes/recipe_form.html", context)

@login_required(login_url="login")
def updateRecipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    form = RecipeForm(instance=recipe)
    form_ing = RecipeIngredientForm(request.POST or None)
    form_meth = RecipeMethodForm(request.POST or None)


    if request.method == 'POST' :
        form = RecipeForm(request.POST,request.FILES, instance=recipe)
        if all([form.is_valid(), form_ing.is_valid(), form_meth.is_valid()]):
            parent = form.save(commit=False)
            parent.save()

            child = form_ing.save(commit=False)
            child.recipe = parent
            child.save()

            child2 = form_meth.save(commit=False)
            child2.recipe = parent
            child2.save()

            form_meth.save(commit=False)
            return redirect('account')

    context = {'form': form, 'form_ing': form_ing, 'form_meth': form_meth}
    return render(request, "recipes/recipe_form.html", context)


@login_required(login_url="login")
def deleteRecipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('account')
    context = {'object': recipe}
    return render(request, 'delete_template.html', context)

def chartRecipe(request):
    recipes, search_query = searchRecipes(request)

    context = {'recipes': recipes}
    return render(request, 'recipes/chart.html' ,context)