from django.urls import path
from  . import views



urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name='home'),
    path('account/logout/', views.logout , name='logout'),
    path('account/signup/', views.signup, name='signup'),
    path('account/login/', views.login, name='login'),
    path('about/', views.about, name="info"),
    path('add_recipe/', views.add, name="add_recipe"),
    path('recipes/', views.add, name="recipes")
    


]

