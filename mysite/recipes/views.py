from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

from recipes.models import Recipe
from recipes.forms import RecipeForm


def index(request):
    # return HttpResponse("Hello, world. You're at the recipes index.")
    context = ''
    return render(request, 'home.html', {
        'context': context
    })
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


class RecipeDetailView(DetailView):
    ''' Renders a specific recipe based on its slug '''
    model = Recipe

    def get(self, request, slug):
        recipe_detail = self.get_queryset().get(slug__iexact=slug)

        return render(request, 'recipe_detail.html', {
            'recipe_detail': recipe_detail
        })


class RecipeAddView(CreateView):
    template_name = 'addrecipe.html'

    def get(self, request):
        form = RecipeForm()
        print('get_method')
        return render(request, 'addrecipe.html', {'form': form})

    def post(self, request):
        form = RecipeForm(request.POST)
        if form.is_valid():
            newrecipe = form.save()
            return HttpResponseRedirect(reverse_lazy('recipe_detail', args[newrecipe.slug]))
        return render(request, 'addrecipe.html', {'form': form})
