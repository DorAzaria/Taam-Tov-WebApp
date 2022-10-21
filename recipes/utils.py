from .models import Recipe, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateRecipes(request, recipes, results):
    page = request.GET.get('page')
    paginator = Paginator(recipes, results)

    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        recipes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        recipes = paginator.page(page)

    leftIndex = (int(page) - 4)
    if leftIndex < 1:
        leftIndex = 1
    
    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)
    return custom_range, recipes

def searchRecipes(request):

    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tags = Tag.objects.filter(name__icontains=search_query)

    projects = Recipe.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(owner__first_name__icontains=search_query) |
        Q(owner__last_name__icontains=search_query) |
        Q(owner__username__icontains=search_query) |
        Q(tags__in=tags)
    )
    return projects, search_query

