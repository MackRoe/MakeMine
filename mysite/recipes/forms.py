from django import forms
from recipes.models import Recipe
from django.forms import ModelForm


class RecipeForm(ModelForm):
    """ Render and process a form based on the Recipe model. """
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions', 'submitter']
