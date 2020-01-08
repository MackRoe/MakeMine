from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from django.urls import reverse


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    catagory = models.CharField(max_length=200, default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    rating = models.IntegerField(default=0)
    slug = models.SlugField(null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/new-recipe-page). """
        path_components = {'slug': self.slug}
        return reverse('recipe_detail', kwargs=path_components)


class Comment(models.Model):
    author = models.CharField(max_length=200)
    comment_text = models.TextField()
