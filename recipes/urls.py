from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipes, name="recipes"),
    path('recipe/<str:pk>/', views.recipe, name="recipe"),

    path('create-recipes/', views.createRecipe, name="create-recipe"),

    path('update-recipes/<str:pk>/', views.updateRecipe, name="update-recipe"),

    path('delete-recipe/<str:pk>/', views.deleteRecipe, name="delete-recipe"),

    path('chart/', views.chartRecipe, name="chart"),
]