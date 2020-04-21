from django.contrib import admin
from recipe.models.models_tag import Tag
from recipe.models.models_ingredient import Ingredient

# Register your models here.
admin.site.register(Tag)
admin.site.register(Ingredient)


