from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipe.models.models_tag import Tag

from recipe.serializers.serializers_tag import TagSerializer

from recipe.views.base_recipe_attributes import BaseRecipeAttrViewSet



class TagViewSet(BaseRecipeAttrViewSet):
    """Manage tags in the database"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

