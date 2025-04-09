from rest_framework import serializers
from .models import Meal, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class MealSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Meal
        fields = '__all__'
