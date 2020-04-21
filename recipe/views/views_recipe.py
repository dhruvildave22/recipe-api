from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipe.models.models_tag import Tag
from recipe.models.models_ingredient import Ingredient 
from recipe.models.models_recipe import Recipe

from recipe.serializers.serializers_ingredient import IngredientSerializer
from recipe.serializers.serializers_recipe import RecipeImageSerializer,\
    RecipeDetailSerializer, RecipeSerializer
from recipe.serializers.serializers_tag import TagSerializer


class RecipeViewSet(viewsets.ModelViewSet):
  """Manage recipes in the database"""
  serializer_class = RecipeSerializer
  queryset = Recipe.objects.all()
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)

  def _params_to_ints(self, qs):
    """Convert a list of string IDs to a list of integers"""
    return [int(str_id) for str_id in qs.split(',')]

  def get_queryset(self):
    """Retrieve the recipes for the authenticated user"""
    tags = self.request.query_params.get('tags')
    ingredients = self.request.query_params.get('ingredients')
    queryset = self.queryset
    if tags:
        tag_ids = self._params_to_ints(tags)
        queryset = queryset.filter(tags__id__in=tag_ids)
    if ingredients:
        ingredient_ids = self._params_to_ints(ingredients)
        queryset = queryset.filter(ingredients__id__in=ingredient_ids)

    return queryset.filter(user=self.request.user)

  def get_serializer_class(self):
    """Return appropriate serializer class"""
    if self.action == 'retrieve':
        return RecipeDetailSerializer
    elif self.action == 'upload_image':
        return RecipeImageSerializer

    return self.serializer_class

  def perform_create(self, serializer):
    """Create a new recipe"""
    serializer.save(user=self.request.user)

  @action(methods=['POST'], detail=True, url_path='upload-image')

  def upload_image(self, request, pk=None):
    """Upload an image to a recipe"""
    recipe = self.get_object()
    serializer = self.get_serializer(recipe, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
