from django.contrib import admin
from recipe.models.models_tag import Tag
from recipe.models.models_ingredient import Ingredient
from recipe.models.models_recipe import Recipe

# Register your models here.
admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe)


