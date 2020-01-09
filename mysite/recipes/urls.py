from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView, RecipeAddView
from recipes.views import RecipeDeleteView, SkinRecipesView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('skin_recipes/', SkinRecipesView.as_view(), name='skin_recipes'),
    path('recipe_list/', RecipeListView.as_view(), name='recipe_list'),
    path('addrecipe/', RecipeAddView.as_view(), name='add_recipe'),
    path('<str:slug>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('<str:slug>/update', RecipeUpdateView.as_view(), name='update_recipe'),
    path('<str:slug>/delete', RecipeDeleteView.as_view(), name='delete_recipe'),
]
