# Generated by Django 2.2.6 on 2020-01-08 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_recipe_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='slug',
            field=models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=600),
        ),
    ]