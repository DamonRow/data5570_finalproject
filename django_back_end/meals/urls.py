from django.urls import path
from .views import meal_search_view  # you can change this if needed

urlpatterns = [
    path('search/', meal_search_view, name='meal_search'),
]
