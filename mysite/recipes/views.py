from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView

from recipes.models import Recipe


def index(request):
    return HttpResponse("Hello, world. You're at the recipes index.")
# Create your views here.


class RecipeListView(ListView):
    ''' Renders a list of all recipes '''
    model = Recipe

    def get(self, request):
        ''' GET a list of recipes '''
        recipe_list = self.get_queryset().all()
        print(recipe_list)
        return render(request, 'recipe_list.html', {
            'recipe_list': recipe_list
        })
