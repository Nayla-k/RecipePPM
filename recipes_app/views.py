from django.shortcuts import render, HttpResponse
from . import models


def home(request):
    return render(request, 'recipes/home.html')

def logout(request):
    return render(request, 'account/logout.html')

def signup(request):
    return render(request, 'account/signup.html')

def login(request):
    return render(request, 'account/login.html')

def about(request):
  return render(request,"recipes/about.html")

def add(request):
  return render(request,"recipes/add_recipe.html")


