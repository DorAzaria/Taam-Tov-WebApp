from django.core import paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from recipes.utils import searchRecipes , paginateRecipes

from django.contrib.auth.decorators import login_required

def homepage(request):
    recipes, search_query = searchRecipes(request)

    context = {'recipes': recipes}
    return render(request, '../templates/homepage.html', context)