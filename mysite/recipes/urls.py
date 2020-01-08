from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_list/', RecipeListView.as_view(), name='recipe_list'),
    path('<str:slug>', RecipeDetailView.as_view(), name='recipe_detail'),
]
