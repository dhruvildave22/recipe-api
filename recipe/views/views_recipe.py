from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipe.models.models_recipe import Recipe
from recipe.serializers.serializers_recipe import RecipeSerializer,\
                    RecipeDetailSerializer, RecipeImageSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
    

    def get_queryset(self):
        """Retrieve the recipes for the authenticated user"""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
      """Return appropriate serializer class"""
      if self.action == 'retrieve':
          return RecipeDetailSerializer
      elif self.action == 'upload_image':
        return RecipeImageSerializer
      return self.serializer_class

    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
      """Upload an image to a recipe"""
      recipe = self.get_object()
      serializer = self.get_serializer(
          recipe,
          data=request.data
      )

      if serializer.is_valid():
          serializer.save()
          return Response(
              serializer.data,
              status=status.HTTP_200_OK
          )

      return Response(
          serializer.errors,
          status=status.HTTP_400_BAD_REQUEST
      )