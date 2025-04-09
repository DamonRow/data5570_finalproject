from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("<h1>Welcome to the Smart Meal Planner 🍽️</h1><p>You're on the home page!</p>")

from django.http import HttpResponse

def meal_search_view(request):
    return HttpResponse("This is the meal search page!")


# Create your views here.
from rest_framework import viewsets
from .models import Meal, Ingredient
from .serializers import MealSerializer, IngredientSerializer

class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
