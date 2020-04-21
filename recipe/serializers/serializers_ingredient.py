
from rest_framework import serializers

from recipe.models.models_ingredient import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Ingredient
        fields = ('id', 'name')
        read_only_Fields = ('id',)