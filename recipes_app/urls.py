from django.contrib import admin


from django.urls import path,include
from . import views


urlpatterns = [

    path('djrichtextfield/', include('djrichtextfield.urls')),
    
    path("", views.RecipeListView.as_view(), name="home"),
    path("home/", views.RecipeListView.as_view(), name="home"),
    path("add_recipe/", views.AddRecipe.as_view() , name="add_recipe"),
    path("recipes/", views.Recipes.as_view(), name="recipes"),
    path("<slug:pk>/", views.RecipeDetail.as_view(), name="recipe_details"),
    path("delete/<slug:pk>/", views.DeleteRecipe.as_view() , name="delete_recipe"),
    path("edit/<slug:pk>/", views.EditRecipe.as_view() , name="edit_recipe"),
]
