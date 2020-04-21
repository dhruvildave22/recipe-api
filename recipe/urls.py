from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipe.views.views_tag import TagViewSet
from recipe.views.views_ingredient import IngredientViewSet


router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]