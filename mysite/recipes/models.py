from django.db import models


# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    catagory = models.CharField(max_length=200, default='')
    ingredients = models.TextField(default='')
    instructions = models.TextField(default='')
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.CharField(max_length=200)
    comment_text = models.TextField()
