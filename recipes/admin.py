from django.contrib import admin
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth import get_user_model

# Register your models here.
from .models import Recipe, Comment, Tag, RecipeIngredient, RecipeMethod

User = get_user_model()
admin.site.unregister(User)

class RecipeInline(admin.StackedInline):
    model = Recipe
    extra = 0

class UserAdmin(admin.ModelAdmin):
    inlines = [RecipeInline]
    list_display = ['username']

admin.site.register(User, UserAdmin)

class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    fields = ['name', 'quanity', 'unit', 'direction']
    extra = 0

class RecipeMethodInline(admin.StackedInline):
    model = RecipeMethod
    fields = ['description', 'direction'] 
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [ RecipeIngredientInline,RecipeMethodInline]
    list_display = ['title','owner']
    readonly_fields = ['created']
    raw_id_fields = ['owner']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Comment)
admin.site.register(Tag)

