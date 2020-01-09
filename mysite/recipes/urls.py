from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView, RecipeAddView, RecipeDeleteView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_list/', RecipeListView.as_view(), name='recipe_list'),
    path('<str:slug>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('addrecipe/', RecipeAddView.as_view(), name='add_recipe'),
    path('<str:slug>/delete', RecipeDeleteView.as_view(), name='delete_recipe'),
]
