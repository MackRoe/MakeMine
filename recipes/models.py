import datetime

from django.db import models
from django.utils.text import slugify
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
# from django.contrib.auth.models import User


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    catagory = models.CharField(max_length=200, default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    rating = models.IntegerField(default=0)
    slug = models.SlugField(null=True)
    submitter = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page (/new-recipe-page). """
        path_components = {'slug': self.slug}
        return reverse('recipe_detail', kwargs=path_components)

    def save(self, *args, **kwargs):
        ''' Creates a URL safe slug automatically when new recipe is added '''
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on superclass
        return super(Recipe, self).save(*args, **kwargs)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # @register.filter(name='split')
    # def split(value, arg):
    #     return value.split(arg)


class Comment(models.Model):
    author = models.CharField(max_length=200)
    comment_text = models.TextField()
