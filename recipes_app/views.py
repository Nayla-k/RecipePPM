from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import CreateView,ListView, DetailView, DeleteView, UpdateView

from django.shortcuts import render, HttpResponse, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.db.models import Q

from recipes_app.forms import RecipeForm
from . import models


class Recipes(ListView):
    """View Recipes"""

    template_name = "recipes/recipes.html"
    model = models.Recipe
    context_object_name = "recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get('q')
        if query:
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(instructions__icontains=query) |
                Q(cuisine_types__icontains=query)
            )
        else:
            recipes = self.model.objects.all()
        return recipes


class RecipeDetail(DetailView):
    """View Recipe Details"""

    template_name = "recipes/recipe_details.html"
    model = models.Recipe
    context_object_name = "recipe"


class RecipeListView(ListView):
    model = models.Recipe
    template_name = "recipes/home.html"


class AddRecipe(LoginRequiredMixin, CreateView):
    """Add recipe view"""

    template_name = "recipes/add_recipe.html"
    model = models.Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)
    
class DeleteRecipe(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Delete a recipe"""
    model = models.Recipe
    success_url = '/recipes/'
    
    template_name = "recipes/recipe_confirm_delete.html"

    def test_func(self):
        return self.request.user == self.get_object().user
    
class EditRecipe(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    """Edit recipe"""
    model = models.Recipe
    success_url = '/recipes/'
    form_class = RecipeForm
    template_name = "recipes/edit_recipe.html"

    def test_func(self):
        return self.request.user == self.get_object().user

    
